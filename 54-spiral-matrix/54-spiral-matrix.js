/**
 * @param {number[][]} matrix
 * @return {number[]}
 */

var spiralOrder = function(matrix) {
    let result = []
    const helper = (boundingBox) => {
        const [[top, left], [bottom, right]] = boundingBox
        if(top > bottom || left > right) return
        
        if(top === bottom && right === left){
            result.push(matrix[top][left])
            return
        }
        
        if(top === bottom){
            for(let i = left; i <= right; i++){
                result.push(matrix[top][i])
            }
            return
        }
        
        if(left === right){
            for(let i = top; i <= bottom; i++){
                result.push(matrix[i][right])
            }
            return
        }
        
        for(let i = left; i < right; i++){
            result.push(matrix[top][i])
        }
        
        for(let i = top; i < bottom; i++){
            result.push(matrix[i][right])
        }
        
        for(let i = right; i > left; i--){
            result.push(matrix[bottom][i])
        }
        
        for(let i = bottom; i > top; i--){
            result.push(matrix[i][left])
        }
        helper([[top + 1, left + 1],[bottom - 1, right - 1]])
    }
    
    helper([[0,0],[matrix.length - 1, matrix[0].length - 1]])
    return result
};