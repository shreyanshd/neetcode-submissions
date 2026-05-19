class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                ans[i1 + i2] += int(num1[i1]) * int(num2[i2])
        
        for i in range(len(ans) - 1):
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
        
        ans = ans[::-1]
        start = 0
        while start < len(ans) and ans[start] == 0:
            start += 1
        ans = map(str, ans[start:])
        return "".join(ans)