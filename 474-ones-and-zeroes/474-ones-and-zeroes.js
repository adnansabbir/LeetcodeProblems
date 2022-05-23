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
    
    const dp = new Array(m+1).fill(0).map(c => new Array(n+1).fill(0).map(d=> new Array(strs.length).fill(0)))
    // console.log(dp)
    const take = (idx, zeros, ones) => {
        if(dp[zeros][ones][idx] > 0) return dp[zeros][ones][idx]
        if(idx === strs.length || zeros + ones === 0) return 0
        const count = freq(idx)
        
        // consider current one
        let consider = 0
        if(zeros >= count[0] && ones >= count[1]){
            consider = 1 + take(idx + 1, zeros - count[0], ones - count[1])
        }
        
        const skip = take(idx + 1, zeros, ones)
        
        dp[zeros][ones][idx] = Math.max(consider, skip)
        return dp[zeros][ones][idx]
    }
    
    return take(0, m, n)
};