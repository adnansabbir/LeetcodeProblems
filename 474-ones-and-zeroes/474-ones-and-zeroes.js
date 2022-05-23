/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    const memo = {}
    const freq = (idx) => {
        if(memo[strs[idx]]) return memo[strs[idx]]
        
        let result = [0,0]
        for(let i = 0; i < strs[idx].length; i++){
            result[0] += strs[idx][i] === '0' ? 1 : 0
            result[1] += strs[idx][i] === '1' ? 1 : 0
        }
        memo[strs[idx]] = result
        return result
    }
    
    const dp = new Array(m+1).fill(0).map(c => new Array(n+1).fill(0))
    
    for(let i = 0; i < strs.length; i++){
        const count = freq(i)
        for(let zeros = m; zeros >= count[0]; zeros--){
            for(let ones = n; ones >= count[1]; ones--){
                dp[zeros][ones] = Math.max(1 + dp[zeros - count[0]][ones - count[1]], dp[zeros][ones])
            }   
        }
    }
    
    return dp[m][n]
    
};