function calculate(s: string): number {
    const isDigit = (char: string): boolean => !isNaN(parseInt(char))
    const stack = [0]
    let num = 0, sign = 1
    for(let i = 0; i < s.length; i++){
        if(s[i] === ' ') continue
        else if(isDigit(s[i])){
            num = num*10 + parseInt(s[i])
        }

        else if(s[i] === '+'){
            stack[stack.length - 1] += num * sign
            sign = 1
            num = 0
        }

        else if(s[i] === '-'){
            stack[stack.length - 1]  += num * sign
            sign = -1
            num = 0
        }

        else if(s[i] === '('){
            stack.push(sign)
            stack.push(0)
            sign = 1
            num = 0
        }

        else if(s[i] === ')'){
            const lastNum = (stack.pop() + (sign * num)) * stack.pop()
            stack[stack.length-1] += lastNum
            sign = 1
            num = 0
        }
    }


    return stack[stack.length-1] + (num * sign)
};