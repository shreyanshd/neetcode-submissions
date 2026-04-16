class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        for n in nums:
            numToFreq[n] = 1 + numToFreq.get(n, 0)
        
        freqBucket = [[] for _ in range(len(nums)+1)]
        for n, f in numToFreq.items():
            freqBucket[f].append(n)
        
        topK = []
        for i in range(len(freqBucket) -1, 0, -1):
            for n in freqBucket[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK
        return topK