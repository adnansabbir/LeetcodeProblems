/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let max_pal = ''
    
    const palindromeLength = (start, end)=> {
        if(start < 0 || end >= s.length) return 0
        return s[start] === s[end] ? 2  + palindromeLength(start - 1, end + 1): 0 
    }
    
    for(let i = 0; i < s.length - (max_pal.length/2); i++){
        const first = palindromeLength(i, i) - 1
        const second = palindromeLength(i, i + 1)
        
        if(first > max_pal.length){
            max_pal = s.slice(i - parseInt(first/2), i + parseInt(first/2) + 1)
        }
        
        // console.log(i, first, second, max_pal, first >= max_pal.length)
        
        if(second > max_pal.length){
            max_pal = s.slice(i - parseInt(second/2) + 1, i + parseInt(second/2) + 1)
        }
        // console.log(i, first, second, max_pal,  second >= max_pal.length)
    }
    
    return max_pal
};