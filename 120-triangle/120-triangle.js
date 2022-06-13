/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    const memo = {}
    const traverse = ( i, j) => {
        const key = `${i}-${j}`
        if(memo[key] !== undefined) return memo[key]
        if(i === triangle.length - 1){
            return triangle[i][j]
        }
        
        memo[key] = triangle[i][j] + Math.min(traverse(i+1, j), traverse(i+1, j+1))
        return memo[key]
    }
    
    const result = traverse(0,0)
    return result
    
};