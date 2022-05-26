/**
 * @param {number[][]} envelopes
 * @return {number}
 */
var maxEnvelopes = function(E) {
    const compare = (a, b) => {
        if(a[0] === b[0]) return b[1] - a[1]
        return a[0] - b[0]
    }
    
    E.sort(compare)
    
    let len = E.length, dp = []
    
    for(let i = 0; i < len; i++){
        let height = E[i][1], left = 0, right = dp.length
        while(left < right){
            let mid = (left + right) >> 1
            if(dp[mid] < height) left = mid + 1
            else right = mid
        }
        dp[left] = height
    }
    
    return dp.length
};