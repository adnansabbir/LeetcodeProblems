/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding = function(words) {
    const keptWords = new Set(words)
    for(let word of words){
        for(let i = 1; i < word.length; i++){
            keptWords.delete(word.substring(i))
        }
    }
    
    let result = 0
    for (let word of keptWords){
        result += word.length + 1
    }
    
    return result
};