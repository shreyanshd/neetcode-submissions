class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        stack = []
        for token in tokens:
            if token in operators:
                sign = token
                b = stack.pop()
                a = stack.pop()
                fn = operators[sign]
                result = fn(a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()