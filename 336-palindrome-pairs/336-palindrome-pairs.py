class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        arr=[]
        hashmap={}
        
        #Adding All words in HashTable
        for i,word in enumerate(words):
            hashmap.update({word:i})
        
        #Case1: when empty string is present in list and words are palindrome by defaults -> eg: ['aba',""]
        if("" in hashmap):
            idx=hashmap[""]
            for i,word in enumerate(words):
                if(idx!=i and word==word[::-1]):
                    arr.append([i,idx])
                    arr.append([idx,i])
        
        #Case2: When Exact word palindrome are present in list after form that word itself.
        #EG: [abc,cba,a] -> [[0,1],[1,0]]
        for i,word in enumerate(words):
            if(word[::-1] in hashmap and hashmap[word[::-1]]!=i):
                idx=hashmap[word[::-1]]
                arr.append([i,idx])
        
        #Case3:
        # When              word2       + palindrome(word1(left))    + word1(right) is Palindrome
        #EG: [sssll,lls] -> lls(word2)  + plaindrome(ss(word1_left)) + sll(word1)
		############################# AND ##############################
        # When              word1(left)     + palindrome(word1(right))    + word2  is Palindrome
        #EG: [llsss,sll] -> lls(word1_left) + plaindrome(ss(word1_right)) + sll(word2)
		
        for i,word in enumerate(words):
            for j in range(1,len(word)):
                left=word[:j]                         #left of word
                right=word[j:]                        #right of word
                if(left==left[::-1]):                 #When palindrome(word1(left))
                    temp=right[::-1]
                    if(temp in hashmap):              #check for right part of word in list
                        arr.append([hashmap[temp],i]) #i.e word2+word1
                if(right==right[::-1]):               #palindrome(word1(right))
                    temp=left[::-1]
                    if(temp in hashmap):              #check for left part of word in list
                        print(word,left,right)
                        arr.append([i,hashmap[temp]]) #i.e word1+word2
                
        return arr