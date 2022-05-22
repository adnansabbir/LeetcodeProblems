/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let totalPalindrome = 0
    
    const getPalindromeCount = (start, end) => {
        if(start < 0 || end >= s.length) return
        else if(s[start] === s[end]){
            totalPalindrome++
            getPalindromeCount(start - 1, end + 1)
        }
    }
    
    for(let i = 0; i < s.length; i++){
        getPalindromeCount(i,i)
        getPalindromeCount(i,i+1)
    }
    
    return totalPalindrome
};