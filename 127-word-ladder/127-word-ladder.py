class Solution:
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        available_words = set(wordList)
        queue = [beginWord]
        
        depth = 0
        while queue:
            depth+=1
            cl = len(queue)
            while cl:
                cl -= 1
                word = queue.pop(0)
                
                for i in range(len(word)):
                    for l in self.letters:
                        nextWord = word[:i]+l+word[i+1:]
                        
                        if nextWord in available_words:
                            available_words.remove(nextWord)
                            if nextWord == endWord:
                                return depth+1
                            queue.append(nextWord)
            
            
        return 0