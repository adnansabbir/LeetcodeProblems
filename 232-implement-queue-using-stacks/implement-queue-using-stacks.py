class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        while self.stack:
            self.aux.append(self.stack.pop())
        res = self.aux.pop()
        while self.aux:
            self.stack.append(self.aux.pop())
        return res
    
    def peek(self):
        return self.stack[0]

    def empty(self):
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()