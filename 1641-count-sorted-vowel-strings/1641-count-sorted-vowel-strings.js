/**
 * @param {number} n
 * @return {number}
 */

const vowels = ['a','e','i','o','u']

const backTrack = (word, idx, n) => {
    if(word.length === n) return 1
    if(idx === 5) return 0
    return backTrack(word + vowels[idx], idx, n) + backTrack(word, idx + 1, n)
}

var countVowelStrings = function(n) {
    if(n === 1) return 5
    
    return backTrack("", 0, n)
};