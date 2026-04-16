class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        num = ""
        for i in range(0, len(s)):
            if (s[i] != "#"):
                 num += s[i]
            else:
                length = int(num)
                nextIndex = i+1+length
                decoded.append(s[i+1:nextIndex])
                if (nextIndex < len(s)):
                    right = self.decode(s[nextIndex:])
                    for r in right:
                        decoded.append(r)
                return decoded

        return decoded
