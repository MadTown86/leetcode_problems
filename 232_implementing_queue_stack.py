# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        if x:
            self.data.append(x)

    def pop(self) -> int:
        return self.data.pop(0)

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        if self.data:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()