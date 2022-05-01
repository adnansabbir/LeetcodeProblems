/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

const getText = (s) => {
    const stack = []
    
    for(let i = 0; i < s.length; i++){
        if(s[i] === '#'){
            if(stack.length){
                stack.pop()
            }
        }else{
            stack.push(s[i])
        }
    }
    
    return stack.join('')
}
var backspaceCompare = function(s, t) {
    return getText(s) === getText(t)
};