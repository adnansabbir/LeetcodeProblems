/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let o = 0
    let c = 0
    
    let maxLength = 0
    for(let i = 0; i < s.length; i++){
        if(s[i] === '(') o++
        else c++
        
        if(o === c) maxLength = Math.max(maxLength, o + c)
        if(c > o){
            o = 0
            c = 0
        }
    }
    
    o = 0
    c = 0
    for(let i = s.length - 1; i >= 0; i--){
        if(s[i] === '(') o++
        else c++
        
        if(o === c) maxLength = Math.max(maxLength, o + c)
        if(c < o){
            o = 0
            c = 0
        }
    }
    
    return maxLength
};