class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = 0
        start = 0

        while count < n:
            i = start
            prev = nums[start]
            while True:
                j = (i + k) % n
                temp = nums[j]
                nums[j] = prev
                prev = temp
                i = j
                count += 1

                if i == start:
                    break
            
            start += 1