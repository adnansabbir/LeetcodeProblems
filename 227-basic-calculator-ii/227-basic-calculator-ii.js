/**
 * @param {string} s
 * @return {number}
 */

const isDigit = (c) => {
    return c.charCodeAt(0) >= 48 && c.charCodeAt(0) < 58
}

var calculate = function(s) {
    const stack = []
    let currentNum = ""
    let operation = ""
    
    for(let i = 0; i < s.length; i++){
        if(isDigit(s[i])){
            currentNum += s[i]
        }
        
        if((!isDigit(s[i]) && s[i] !== ' ') || i === s.length - 1){
            switch(operation){
                case '+':
                    stack.push(parseInt(currentNum))
                    break
                case '-':
                    stack.push(parseInt(currentNum) * -1)
                    break
                case '*':
                    stack.push(stack.pop() * parseInt(currentNum))
                    break
                case '/':
                    stack.push(parseInt(stack.pop() / parseInt(currentNum)))
                    break
                default:
                    stack.push(parseInt(currentNum))
            }
            operation = s[i]
            currentNum = ""
        }
    }
    
    let result = 0
    while(stack.length){
        result += stack.pop()
    }
    return result
};