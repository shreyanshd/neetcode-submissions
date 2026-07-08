class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # (index, num)
        output = []

        for i in range(0, len(nums)):
            # remove for left of Q if index is out of window
            while q and (i - q[0][0]) >= k:
                q.popleft()

            # remove from right of Q if num is smaller than num
            num = nums[i]
            while q and q[-1][1] <= num:
                q.pop()
            
            # append (index, num) to right of Q
            q.append((i, num))

            # collect leftmost num from Q in output
            if i >= k - 1:
                output.append(q[0][1])

        return output