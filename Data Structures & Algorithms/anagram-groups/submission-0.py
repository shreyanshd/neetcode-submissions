class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for s in strs:
            key = str(sorted(s))
            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(s)
        anagrams = [group for group in anagramMap.values()]
        return anagrams