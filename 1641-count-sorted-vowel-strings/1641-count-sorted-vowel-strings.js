/**
 * @param {number} n
 * @return {number}
 */

const backTrack = (count, idx, n) => {
    if(count === n) return 1
    if(idx === 5) return 0
    return backTrack(count+1, idx, n) + backTrack(count, idx + 1, n)
}

var countVowelStrings = function(n) {
    if(n === 1) return 5
    
    return backTrack(0, 0, n)
};