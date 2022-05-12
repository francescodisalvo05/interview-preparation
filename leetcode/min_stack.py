# 155 - https://leetcode.com/problems/min-stack/

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # space = O(n) | time = O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    # space = O(n) | time = O(1)
    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.min_stack[-1]:
            self.min_stack.pop()

    # space = O(n) | time = O(1)
    def top(self) -> int:
        return self.stack[-1]
    
    # space = O(n) | time = O(1)
    def getMin(self) -> int:
        return self.min_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()