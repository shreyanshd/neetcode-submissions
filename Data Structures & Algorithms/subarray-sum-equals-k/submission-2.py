class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        currSum = 0
        total = 0
        for num in nums:
            prefixSum[currSum] += 1
            currSum += num
            total += prefixSum[currSum - k]
        return total
            

