/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    while(b){
        let c = (a&b) <<1
        a = a ^ b
        b = c
    }
    
    return a
};