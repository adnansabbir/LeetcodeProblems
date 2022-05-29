/**
 * @param {string[]} words
 * @return {number}
 */

const getBit = (a) => {
    let result = new Array(26).fill(0)
    for(let i = 0; i< a.length; i++){
        const idx = a.charCodeAt(i) - 97
        result[idx] = 1
    }
    // return result
    return parseInt(result.join(''), 2)
}

var maxProduct = function(words) {
    const bits = words.map(word => getBit(word))
    let result = 0
    for(let i = 0; i < bits.length; i++){
        for(let j = i + 1; j < bits.length; j++){
            if(!(bits[i] & bits[j])){
                result = Math.max(result, words[i].length * words[j].length)
            }
        }
    }
    
    return result
};