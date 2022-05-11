/**
 * @param {number} n
 * @return {number}
 */

var countVowelStrings = function(n) {
    if(n === 1) return 5
    const dp = new Array(n+1).fill(0).map(() => new Array(5).fill(0))
    for(let i = 0; i < 5; i++){
        dp[1][i] = 1
    }
    
    let sum = 5
    
    for(let i = 2; i < dp.length; i++){
        dp[i][0] = sum
        for(let j = 1; j < 5; j++){
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
            sum += dp[i][j]
        }
    }
    
    return sum
};