/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets = function(words1, words2) {
    
    // f = 26
    const frequency = {}
    
    // m = word2 length
    // i = average length of word in word 2
    // O(m*i)
    for(let i = 0; i < words2.length; i++){
        const tempFreq = {}
        for (let j = 0; j < words2[i].length; j++){
            const char = words2[i][j]
            tempFreq[char] = (tempFreq[char] || 0) + 1
        }
        
        Object.keys(tempFreq).forEach(key=> {
            if(!frequency[key]){
                frequency[key] = tempFreq[key]
            }else{
                frequency[key] = Math.max(frequency[key], tempFreq[key])
            }
        })
    }
    
    const totalChars = Object.values(frequency).reduce((a,b)=> a + b, 0)

    
    const matched = (word) => {
        let tempTotal = totalChars
        const tempFreq = {...frequency}
        for(let char of word){
            if(tempFreq[char]){
                tempTotal -=1
                tempFreq[char] -=1
            }
            
            if(!tempTotal) return true
        }
        
        return false
    }
    
    return words1.filter(word => matched(word))
    
};