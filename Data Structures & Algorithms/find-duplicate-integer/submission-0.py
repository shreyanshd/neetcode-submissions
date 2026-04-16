class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = set()
        for n in nums:
            if n in m: return n
            else: m.add(n)
        return -1