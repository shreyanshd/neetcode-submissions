class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1

        while True:
            i = l + (r - l) // 2    # A
            j = half - (i+1) - 1    # B

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            # found median
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1: #odd
                    median = min(Aright, Bright)
                else: #even
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return median
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
