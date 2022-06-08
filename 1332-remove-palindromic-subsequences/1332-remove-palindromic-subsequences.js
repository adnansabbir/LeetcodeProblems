/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    return !s ? 0 : s === s.split('').reverse().join('') ? 1 : 2
};