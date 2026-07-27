class MinStack:

    def __init__(self):
        self.stack : list(int) = []
        self.min_stack : list(int) = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and  val <= self.min_stack[-1]:
            self.min_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = 0
        min_top_val = 0
        if self.stack:
            val = self.stack[-1]
        if self.min_stack:
            min_top_val = self.min_stack[-1]
        
        if val == min_top_val and self.stack and self.min_stack:
            self.min_stack.pop()
            self.stack.pop()
        elif self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else 0
        
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else 0
        
