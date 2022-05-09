# 232 - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    
    # space = O(n)
    def __init__(self):
        self.queue = []
        
    # time = O(1)
    def push(self, x: int) -> None:
        """Push x to the back of the queue"""
        self.queue.append(x)
        
    # time = O(1)
    def pop(self) -> int:
        """Removes the element from the front and returns it"""
        return self.queue.pop(0)
    
    # time = O(1)
    def peek(self) -> int:
        """Returns the element at the front of the queue"""
        return self.queue[0]
        
    # time = O(n)
    def empty(self) -> bool:
        """Returns True if queue is empty"""
        return True if not self.queue else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()