class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        min_prod, max_prod = 1, 1
        
        for num in nums:
            if num < 0:
                min_prod, max_prod = max_prod, min_prod
            
            min_prod = min(num, num * min_prod)
            max_prod = max(num, num * max_prod)

            result = max(result, max_prod)

        return result