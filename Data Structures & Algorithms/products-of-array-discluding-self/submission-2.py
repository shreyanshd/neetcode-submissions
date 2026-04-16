class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
        
        right = [1] * n
        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i]
    
        product = []    
        for i in range(n):
            if i == 0:
                product.append(right[i+1])
            elif i == n-1:
                product.append(left[i-1])
            else:
                product.append(left[i-1] * right[i+1])
        return product

        
