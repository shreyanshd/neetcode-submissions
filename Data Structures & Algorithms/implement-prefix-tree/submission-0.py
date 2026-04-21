class PrefixTree:

    def __init__(self):
        self.trie = {}
        self.EOW = "EOW"

    def insert(self, word: str) -> None:
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t[self.EOW] = True

    def search(self, word: str) -> bool:
        t = self.trie
        for char in word:
            if char not in t:
                return False
            t = t[char]
        return self.EOW in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for p in prefix:
            if p not in t:
                return False
            t = t[p]
        return True
        