class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        for i, n in enumerate(nums):
            leftNums = nums[0:i]
            rightNums = nums[i+1:len(nums)]
            pairs = self.twoSum(leftNums + rightNums, -n)
            for pair in pairs:
                arr = [n, pair[0], pair[1]]
                triples.add(tuple(sorted(arr)))
        
        result = [row for row in triples]
        return result

    def twoSum(self, nums: List[int], target):
        hashMap = {}
        for n in nums:
            if n not in hashMap: hashMap[n] = 0
            hashMap[n] += 1

        pairs = []
        for n in nums:
            hashMap[n] -= 1
            m = target - n
            if m in hashMap and hashMap[m] > 0:
                hashMap[m] -= 1
                pairs.append([n, m])
            else:
                hashMap[n] += 1
        return pairs        