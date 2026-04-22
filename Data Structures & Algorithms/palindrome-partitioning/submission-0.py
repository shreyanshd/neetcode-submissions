class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(i, curr):
            if i == len(s):
                result.append(curr.copy())
                return 
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    curr.append(s[i:j + 1])
                    dfs(j + 1, curr)
                    curr.pop()
        
        dfs(0, [])
        return result

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
