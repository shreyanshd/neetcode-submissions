class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        for n in nums:
            numToFreq[n] = 1 + numToFreq.get(n, 0)
        
        freqToNum = defaultdict(list)
        for num, freq in numToFreq.items():
            freqToNum[freq].append(num)

        res = []
        for f in sorted(freqToNum.keys(), reverse=True):
            res.extend(freqToNum[f])
        topK = res[:k]
        return topK