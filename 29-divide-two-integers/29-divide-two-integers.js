/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    const result = dividend/divisor
    if(result > 2147483647) return 2147483647
    if(result < -2147483648) return -2147483648
    return parseInt(result)
};