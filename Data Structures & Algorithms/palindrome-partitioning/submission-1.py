class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, curr):
            if i == len(s):
                result.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    curr.append(s[i:j + 1])
                    dfs(j + 1, curr)
                    curr.pop()

        dfs(0, [])
        return result