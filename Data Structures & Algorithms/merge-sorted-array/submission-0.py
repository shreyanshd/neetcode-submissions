class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = len(nums1)
        i = n - 1
        j = m - 1
        while j >= 0:
            nums1[i] = nums1[j]
            i -= 1
            j -= 1
        
        i += 1
        j = 0
        k = 0

        while i < n and j < n-m:
            minVal = 0
            if nums1[i] < nums2[j]:
                minVal = nums1[i]
                i += 1
            else:
                minVal = nums2[j]
                j += 1
            nums1[k] = minVal
            k += 1
        
        while i < n:
            nums1[k] = nums1[i]
            i += 1
            k += 1

        while j < n-m:
            nums1[k] = nums2[j]
            j += 1
            k += 1

        