class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if len(count) <= 2:
                continue
            
            tmp_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    tmp_count[num] = c - 1
            count = tmp_count
        
        result = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                result.append(n)
        return result
        