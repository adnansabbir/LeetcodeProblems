/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const chars = new Set()
    let start = 0
    let max_len = 0
    
    for(let end = 0; end < s.length; end++){
        while(chars.has(s[end])){ 
             chars.delete(s[start++])     
        }
        
        chars.add(s[end])
        max_len = Math.max(max_len, end - start + 1)
    }

    return max_len
};