/**
 * @param {string} expression
 * @return {number[]}
 */

const calculate = (num1, num2, oper) => {
    if(oper === '+') return parseInt(num1) + parseInt(num2)
    if(oper === '-') return parseInt(num1) - parseInt(num2)
    if(oper === '*') return parseInt(num1) * parseInt(num2)
}

var diffWaysToCompute = function(exp) {
    const evaluate = (exp) => {
        let res = []
        
        for(let i = 0; i < exp.length; i++){
            if(exp[i] === '+' || exp[i] === '-' || exp[i] === '*'){
                const left = evaluate(exp.substring(0, i))
                const right = evaluate(exp.substring(i + 1, exp.length + 1))
                for(let l of left){
                    for(let r of right){
                        res.push(calculate(l, r, exp[i]))
                    }
                }
            }
        }
        
        return res.length ? res : [exp]
    }
    
    return evaluate(exp)
};