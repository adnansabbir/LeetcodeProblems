class TrieNode{
    constructor(){
        this.children = new Map()
        this.weight = 0
    }
}

class WordFilter{
    constructor(words){
        this.trie = new TrieNode()
        let weight = 0
        
        for(let word of words){
            let currTrie = this.trie
            currTrie.weight = weight
            const L = word.length
            for(let i = 0; i < L; i++){
                let tempTrie = currTrie
                for(let j = i; j<L; j++){
                    // 96 is the char code of character `
                    const code = (word.charCodeAt(j) - 96) * 27
                    if(tempTrie.children.get(code) === undefined) tempTrie.children.set(code, new TrieNode())
                    tempTrie = tempTrie.children.get(code)
                    tempTrie.weight = weight
                }
                
                tempTrie = currTrie
                for(let j = L - i - 1; j >= 0; j--){
                    // 96 is the char code of character `
                    const code = (word.charCodeAt(j) - 96)
                    if(tempTrie.children.get(code) === undefined) tempTrie.children.set(code, new TrieNode())
                    tempTrie = tempTrie.children.get(code)
                    tempTrie.weight = weight
                }
            
                const code = ((word.charCodeAt(i) - 96) * 27) + (word.charCodeAt(L - i - 1) - 96)
                if(currTrie.children.get(code) === undefined) currTrie.children.set(code, new TrieNode())
                currTrie = currTrie.children.get(code)
                currTrie.weight = weight
            }
            weight++
        }
    }
    
    f(prefix, suffix){
        // console.log(this.trie)
        let trie = this.trie
        let i = 0, j = suffix.length - 1
        while(i < prefix.length || j >= 0){
            const code1 = i < prefix.length ? prefix.charCodeAt(i) : 96
            const code2 = j >= 0 ? suffix.charCodeAt(j) : 96
            const code = ((code1 - 96) * 27) + (code2 - 96)
            
            trie = trie.children.get(code)
            if(trie === undefined) return -1
            i++ 
            j--
        }
        
        return trie.weight
    }
}

/** 
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(prefix,suffix)
 */