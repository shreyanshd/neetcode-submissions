class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = max(c.values())
        for e, cnt in c.items():
            if cnt == m:
                return e