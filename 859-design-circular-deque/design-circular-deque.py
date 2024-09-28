class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.q = [None] * k
        self._reset()
    
    def _reset(self):
        self.size = 0
        self.head = None
        self.tail = None

    def initialize_pointers(self):
        if not self.head:
            self.head = 0
            self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.head == None:
            self.initialize_pointers()
        else:
            self.head = (self.head + 1) % self.capacity
        
        self.q[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.tail == None:
            self.initialize_pointers()
        else:
            self.tail = self.capacity - 1 if self.tail == 0 else self.tail - 1
        
        self.q[self.tail] = value
        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = self.capacity - 1 if self.head == 0 else self.head - 1
        self.size -= 1

        if self.size == 0:
            self._reset()
        
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        
        if self.size == 0:
            self._reset()
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.tail]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()