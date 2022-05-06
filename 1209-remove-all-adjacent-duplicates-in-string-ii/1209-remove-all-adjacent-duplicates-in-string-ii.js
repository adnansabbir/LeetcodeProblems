/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */

var removeDuplicates = function(s, k) {
    const stack = [s[0]]
    const count = [1]
    
    for(let i = 1; i < s.length; i++){
        stack.push(s[i])
        count.push(s[i] === stack.at(-2) ? count.at(-1) + 1 : 1)

        if(count.at(-1) === k){
            for(let j = 0; j < k; j++){
                stack.pop()
                count.pop()
            }
        }
    }
    
    return stack.join('')
};