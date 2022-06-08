/**
 * @param {string} s
 * @return {number}
 */

var removePalindromeSub = function(s) {
    if(!s) return 0
    
    for(let i = 0; i < s.length; i++){
        if(s[i] !== s[s.length - 1 - i]) return 2
    }
    
    return 1
};