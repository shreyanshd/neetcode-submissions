class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True 

    def search(self, word: str) -> bool:
        
        def dfs(word, i, node):        
            if i == len(word):
                return node.eow
            
            c = word[i]
            if c == ".":
                for m in node.children.values():
                    res = dfs(word, i+1, m)
                    if res: return True
                return False
            elif c not in node.children:
                return False
            else:
                return dfs(word, i+1, node.children[c])

        return dfs(word, 0, self.root)

