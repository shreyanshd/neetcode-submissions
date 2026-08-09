class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            next_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    q = p.copy()
                    q.insert(i, num)
                    next_perms.append(q)
            perms = next_perms
        return perms