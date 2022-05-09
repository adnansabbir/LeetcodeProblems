/**
 * @param {string} digits
 * @return {string[]}
 */

const _map = {
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z']
    }

var letterCombinations = function(digits) {
    if(!digits.length) return []
    const stack = [..._map[digits[0]]]
    
    while(stack[0].length < digits.length){
        const size = stack.length
        const pointer = stack[0].length
        for(let i = 0; i< size; i++){
            const word = stack.shift()
            _map[digits[pointer]].forEach(c => stack.push(word+c))
        }
    }
    
    return stack
};