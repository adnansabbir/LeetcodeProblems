/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n, cache = {0:0, 1:1, 2:2}) {
    let [temp, prev,curr] = [0, 0, 1]
    for(let i = 0; i<n; i++){
        temp = curr
        curr = curr + prev
        prev = temp
    }
    
    return curr
};