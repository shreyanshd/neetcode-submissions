class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            n = digits[i] + carry
            if n == 10:
                n = 0
                carry = 1
            else:
                carry = 0
            result.append(n)
        
        if carry == 1:
            result.append(carry)
        
        result.reverse()
        return result