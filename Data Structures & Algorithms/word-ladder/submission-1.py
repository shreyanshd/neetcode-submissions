class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isValidTransformation(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
            return diff == 1

        wordList.append(beginWord)
        n = len(wordList)
        graph = { word:[] for word in wordList }
        for i in range(n):
            for j in range(i+1, n):
                w1 = wordList[i]
                w2 = wordList[j]
                if isValidTransformation(w1, w2):
                    graph[w1].append(w2)
                    graph[w2].append(w1)
        
        if endWord not in graph:
            return 0
        
        q = collections.deque([beginWord])
        visit = set([beginWord])
        count = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return count
                for nxt in graph[curr]:
                    if nxt not in visit:
                        q.append(nxt)
                        visit.add(nxt)
            count += 1
        
        return 0
        
