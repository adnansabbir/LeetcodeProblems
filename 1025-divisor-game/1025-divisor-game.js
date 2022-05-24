/**
 * @param {number} n
 * @return {boolean}
 */
var divisorGame = function(n, dp = {1: false}) {
    if(dp[n] !== undefined) return dp[n]
    
    for(let i = 1; i * i <= n; i++){
        if(n % i === 0){
            if(divisorGame(n-i, dp) === false){
                dp[n] = true
                return true   
            }
            
            if(i !== 1 && divisorGame(n - (n/i), dp) === false){
                dp[n] = true
                return true   
            }
        }
    }
    dp[n] = false
    return false
};