class MyStack:

    def __init__(self):
        self.cq = []
        
        

    def swapQs(self, val: int):
        self.cq.append(val)
        for i in range(len(self.cq)-1):
            self.cq.append(self.cq.pop(0))
    
    def push(self, x: int) -> None:        
        self.swapQs(x)
        # print(x, self.q1, self.q2, self.cq)
        

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