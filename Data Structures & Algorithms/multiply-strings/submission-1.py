class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        zeros = 0
        for c1 in num1[::-1]:
            temp = []
            for _ in range(zeros):
                temp.append(0)
            carry = 0
            n1 = int(c1)
            for c2 in num2[::-1]:
                n2 = int(c2)
                p = (n1 * n2) + carry
                digit = p % 10
                carry = p // 10
                temp.append(digit)
            if carry != 0:
                temp.append(carry)
            print(temp)
            zeros += 1
            total += self.getNumber(temp)
        
        return str(total)

    def getNumber(self, arr):
        total = 0
        p = 0
        for a in arr:
            total += pow(10, p) * a
            p += 1
        return total