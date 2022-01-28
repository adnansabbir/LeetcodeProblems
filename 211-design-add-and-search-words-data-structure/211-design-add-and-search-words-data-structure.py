class TrieNode:
    def __init__(self):
        self.childs = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.dictionary = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.dictionary
        for char in word:
            if char not in node.childs:
                node.childs[char] = TrieNode()
            node = node.childs[char]
        node.end = True

    def search(self, word: str, node = None) -> bool:
        if not node:
            node = self.dictionary
        
        for i, char in enumerate(word):
            if char in node.childs:
                node = node.childs[char]
            elif char == '.':
                for key, _ in node.childs.items():
                    if self.search(word[i+1:], node.childs[key]):
                        return True
                return False
            else:
                return False
        
        return node.end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)