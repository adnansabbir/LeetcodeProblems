/**
 * @param {string[]} words
 * @return {number}
 */

const hasCommon = (a, b) => {
    const A = new Set(a.split(''))
    for(let i = 0; i < b.length; i++){
        if(A.has(b[i])) return true
    }
    
    return false
}

var maxProduct = function(words) {
    words.sort((a, b) => b.length  - a.length)
    let max_size = 0
    for(let i = 0; i < words.length; i++){
        for(let j = i + 1; j < words.length; j++){
            if(!hasCommon(words[i], words[j])){
                max_size = Math.max(max_size, words[i].length * words[j].length)
            }
        }
    }
    
    return max_size
};