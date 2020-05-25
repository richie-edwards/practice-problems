"""
Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.
Methods pop, top and getMin operations will always
be called on non-empty stacks.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, x: int) -> None:
        if self.min_val is None:
            # tuple (a, b) where a is the value and b is the minimun stack
            # value at that point
            self.stack.append((x, x))
            self.min_val = x
        else:
            self.stack.append((x, min(x, self.min_val)))
            self.min_val = min(x, self.min_val)

    def pop(self) -> None:
        result = self.stack.pop()[0]
        if self.stack:
            self.min_val = self.stack[-1][1]
        else:
            self.min_val = None
        return result

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
