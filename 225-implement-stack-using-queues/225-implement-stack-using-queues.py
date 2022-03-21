class MyStack:

    def __init__(self):
        self.cq = []
        
    
    def push(self, x: int) -> None:        
        self.cq.append(x)
        for i in range(len(self.cq)-1):
            self.cq.append(self.cq.pop(0))
        

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