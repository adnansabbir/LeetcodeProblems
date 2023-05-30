class MyHashSet:

    def __init__(self):
        self.hashTable = set()
        

    def add(self, key: int) -> None:
        self.hashTable.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashTable:
            self.hashTable.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashTable
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)