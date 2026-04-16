class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))

        res = [q[0][0]]
        for i in range(k, len(nums)):
            while q and i - q[0][1] >= k:
                q.popleft()
            while q and nums[i] >= q[-1][0]:
                q.pop()
            q.append((nums[i], i))
            res.append(q[0][0])
        
        return res