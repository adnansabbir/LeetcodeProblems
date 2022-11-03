function longestPalindrome(words: string[]): number {
// lc cl gg gg bb lc

// lc gg bb gg cl lc lc ab ab ababaa
//     commonPair:
//         bb - 0
    
//     uncommonPair:
//         lc - 0
//         gg - 0
//         cl - 0
        
//     lcggbbggcl
    
    const commonPair = {}
    const uncommonPair = {}
    
    for(let word of words){
        if(commonPair[word] === undefined) commonPair[word] = 0
        if(uncommonPair[word] === undefined) uncommonPair[word] = 0
        
        if(word[0] === word[1]){
            commonPair[word]++
            if(commonPair[word] !== 2) continue
            commonPair[word] = 0
            uncommonPair[word] +=2
        }else{
            uncommonPair[word]++   
        }
    }
    let result = Object.values(commonPair).some((val) => val === 1) ? 2 : 0
    // console.log(result,uncommonPair)
    for(let key of Object.keys(uncommonPair)){
        if(!uncommonPair[key]) continue
        if(key[0] === key[1]){
            result += uncommonPair[key] * 2
        }else{
            const oppositeKey = `${key[1]}${key[0]}`
            result += Math.min(uncommonPair[key], (uncommonPair[oppositeKey] || 0)) * 2 * 2
            uncommonPair[oppositeKey] = 0
        }
        uncommonPair[key] = 0
        // console.log(result, uncommonPair)
    }
    
    return result
};