import random

class RandomizedSet:

    def __init__(self):
        self.uniqueData = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.uniqueData:
            return False

        self.data.append(val)
        self.uniqueData[val] = len(self.data) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.uniqueData:
            return False
        
        self.data[self.uniqueData[val]], self.data[-1] = self.data[-1], self.data[self.uniqueData[val]]
        self.uniqueData[self.data[self.uniqueData[val]]] = self.uniqueData[val]
        self.data.pop()
        del self.uniqueData[val]
        return True
        
    def getRandom(self) -> int:
        randIndex = random.randint(0, len(self.data) - 1)
        return self.data[randIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()