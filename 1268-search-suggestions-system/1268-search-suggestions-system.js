class TrieNode{
    constructor(){
        this.childrens = new Map()
        this.rest = []
    }
}

/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
const suggestedProducts = (products, searchWord) => {
    const trie = new TrieNode()
    let tempTrie = trie
    for(let i = 0; i < searchWord.length; i++){
        tempTrie.childrens.set(searchWord[i], new TrieNode())
        tempTrie = tempTrie.childrens.get(searchWord[i])
    }
    
    for(let product of products){
        tempTrie = trie
        for(let i = 0; i < product.length; i++){
            if(tempTrie.childrens.get(product[i]) === undefined){
                tempTrie.rest.push(product.slice(i))
                tempTrie.rest.sort()
                tempTrie.rest.splice(3)
                break
            }
            tempTrie = tempTrie.childrens.get(product[i])
            if(i === product.length - 1){
                tempTrie.rest.push('')
            }
        }
    }
    
    const result = []
    tempTrie = trie
    const traverseAndCollect = (currTrie = tempTrie.childrens.get(searchWord[0]), word = searchWord[0]) =>{
        if(currTrie.childrens.size === 0) return currTrie.rest.map(r => word + r)
        const [nextKey] = currTrie.childrens.keys()
        const currentResult = currTrie.rest.map(r => word + r)
        
        const nextResult = traverseAndCollect(currTrie.childrens.get(nextKey), word + nextKey)
        result.push(nextResult)
        currentResult.push(...nextResult)
        currentResult.sort()
        currentResult.splice(3)
        return currentResult
    }
    
    result.push(traverseAndCollect())
    result.reverse()
    return result
};