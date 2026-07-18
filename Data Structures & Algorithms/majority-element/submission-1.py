class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for n, cnt in c.items():
            if cnt >= math.ceil(len(nums) / 2):
                return n