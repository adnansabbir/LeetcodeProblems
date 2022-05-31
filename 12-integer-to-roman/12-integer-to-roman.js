/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const roman = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    
    const sequence = [1000,500,100,50,10,5,1,0]
    
    const generateRoman = (n, idx = 0) => {
        if(!n) return ""
        const number = sequence[idx]
        const nextNumber = number / 2 === sequence[idx+1] ? sequence[idx+2] : sequence[idx+1]
        let result = ""
        if(n >= number){
            result += new Array(parseInt(n / number)).fill(roman[number]).join('')
            result += generateRoman(n % number, idx)
            
            
        }else if(n >= number - nextNumber){
            result += new Array(parseInt(n / (number - nextNumber))).fill(`${roman[nextNumber]}${roman[number]}`).join('')
            result += generateRoman(n % (number - nextNumber), idx + 1)
        }else{
            result += generateRoman(n, idx + 1)
        }

        return result 
    }
    
    return generateRoman(num)
};