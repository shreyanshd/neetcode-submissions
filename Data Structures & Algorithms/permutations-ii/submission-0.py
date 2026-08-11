class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counts = Counter(nums)

        def dfs(perms):
            if len(perms) == len(nums):
                result.append(perms.copy())
                return

            for num in counts:
                if counts[num] > 0:
                    perms.append(num)
                    counts[num] -= 1
                    dfs(perms)
                    counts[num] += 1
                    perms.pop()

        dfs([])
        return result
