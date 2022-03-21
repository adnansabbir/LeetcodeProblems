class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.cq = self.q1
        
        

    def swapQs(self, val: int):
        if self.q1:
            self.cq = self.q2
            self.q2.append(val)
            while self.q1:
                self.q2.append(self.q1.pop(0))
        else:
            self.cq = self.q1
            self.q1.append(val)
            while self.q2:
                self.q1.append(self.q2.pop(0))
    
    def push(self, x: int) -> None:        
        self.swapQs(x)
        print(x, self.q1, self.q2, self.cq)
        

    def pop(self) -> int:
        return self.cq.pop(0)

    def top(self) -> int:
        return self.cq[0]

    def empty(self) -> bool:
        return len(self.cq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()