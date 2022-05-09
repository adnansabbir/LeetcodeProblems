/**
 * @param {string} digits
 * @return {string[]}
 */

const _map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

var letterCombinations = function(digits) {

    if(!digits.length) return []
    if(digits.length === 1) return _map[digits].split('')

    const chars = _map[digits.charAt(0)].split('')
    const subRes = letterCombinations(digits.substring(1))
    const result = []
    subRes.forEach(sr => {
        chars.forEach(c => result.push(c+sr))
    })
    return result
    
    return result
};