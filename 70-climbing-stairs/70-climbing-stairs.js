/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n, cache = {0:0, 1:1, 2:2}) {
    if(cache[n] !== undefined) return cache[n]
    
    cache[n] = climbStairs(n-1, cache) + climbStairs(n-2, cache)
    return cache[n]
};