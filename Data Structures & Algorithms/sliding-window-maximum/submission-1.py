class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(0, len(nums)):
            while q and i - q[0][1] >= k:
                q.popleft()
            while q and nums[i] >= q[-1][0]:
                q.pop()
            q.append((nums[i], i))
            if i >= k-1:
                res.append(q[0][0])
        
        return res