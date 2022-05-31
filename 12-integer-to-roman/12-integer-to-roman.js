/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    
    const seq = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
    let result = ""
    let i = 0
    while(num){
        if(num >= seq[i]){
            result += roman[seq[i]]
            num -= seq[i]
            continue
        }
        
        i++
    }
    
    return result
};