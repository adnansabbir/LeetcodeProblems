/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets = function(A, B) {
    const count = (word) => {
        const fq = new Array(26).fill(0)
        for(let ch of word){
            fq[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++
        }
        return fq
    }
    
    const BFreq = new Array(26).fill(0)
    
    B.forEach(word=> {
        count(word).forEach((v, i)=> BFreq[i] = Math.max(BFreq[i], v))
    })
    
    const matched = (word) => !count(word).some((v, i) => BFreq[i] > v)
    
    return A.filter(word => matched(word))
    
};