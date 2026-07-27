class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []

        open_ = set("([{")
        closed = set(")]}")

        def _func(char1 : str, char2 : str) -> bool:
            if char1 == '(' and char2 == ')':
                return True
            if char1 == '[' and char2 == ']':
                return True
            if char1 == '{' and char2 == '}':
                return True

            return False

        for index, char in enumerate(s):
            if char in open_:
                stack.append(char)
            elif not stack and char in closed:
                return False
            elif char in closed and _func(stack[-1], char):
                stack.pop()
            elif char in closed and not _func(stack[-1], char): 
                return False

        return True if not stack else False

            


        