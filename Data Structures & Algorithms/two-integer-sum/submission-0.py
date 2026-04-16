class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIndex = {}
        for i, n in enumerate(nums):
            if n not in numsIndex:
                numsIndex[n] = set()
            numsIndex[n].add(i)
        
        for i, n in enumerate(nums):
            x = target - n
            if x in numsIndex:
                for j in numsIndex[x]:
                    if i != j:
                        return [i, j]