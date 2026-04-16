class Solution:
    SEP = '__elem__'

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += self.SEP + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split(self.SEP)[1:]
        return decoded