/**
 * @param {string[]} words
 * @return {number}
 */

const isPredecessor = (pred, word) => {
    if(pred.length !== word.length - 1) return false
    let p = 0
    let w = 0
    let skipped = false
    while(p < pred.length){
        if(pred[p] !== word[w] && skipped) return false
        else if(pred[p] !== word[w]){
            skipped = true
            w++
        }else{
            p++
            w++
        }
    }
    return true
}

var longestStrChain = function(words) {
    const dp = new Array(words.length).fill(0)
    words.sort((a, b) => a.length - b.length)
    
    const createChain = (idx) => {
        if(dp[idx]) return dp[idx]
        const pred = words[idx]
        let idx2 = idx + 1
        while(idx2 < words.length && words[idx2].length === pred.length) idx2++
        while(idx2 < words.length && words[idx2].length === pred.length + 1){
            if(isPredecessor(pred, words[idx2])){
                dp[idx2] = dp[idx2] ? dp[idx2] : createChain(idx2)
                dp[idx] = Math.max(dp[idx], dp[idx2] + 1)
               }
            idx2++
        }
        dp[idx] = dp[idx] ? dp[idx] : 1
        return dp[idx]
    }
    
    let max_chain = 0
    for(let i = 0; i < words.length; i++){
        max_chain = Math.max(max_chain, createChain(i))
    }
    
    return max_chain
};