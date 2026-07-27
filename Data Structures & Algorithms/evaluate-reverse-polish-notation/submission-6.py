class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set("+-*/")

        stack = []

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            if token in ops:
                res = 0
                val1 = stack.pop()
                val2 = stack.pop()

                if token == '+':
                    res = val1+val2
                if token == '*':
                    res = val1*val2
                if token == '/':
                    res = int(val2/val1)
                if token == '-':
                    res = val2 - val1
                stack.append(res)
        return stack[-1] if stack else 0

        