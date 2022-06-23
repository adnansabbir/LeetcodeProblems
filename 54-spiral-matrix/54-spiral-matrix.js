/**
 * @param {number[][]} matrix
 * @return {number[]}
 */

var spiralOrder = function(matrix) {
    let result = []
    let count = matrix.length * matrix[0].length
    let [[top, left], [bottom, right]] = [[0,0],[matrix.length - 1, matrix[0].length - 1]]
    while(count){
        if(top === bottom && right === left){
            result.push(matrix[top][left])
            count--
            break
        }
        
        if(top === bottom){
            for(let i = left; i <= right; i++){
                result.push(matrix[top][i])
                count--
            }
            break
        }
        
        if(left === right){
            for(let i = top; i <= bottom; i++){
                result.push(matrix[i][right])
                count--
            }
            break
        }
        
        for(let i = left; i < right; i++){
            result.push(matrix[top][i])
            count--
        }
        
        for(let i = top; i < bottom; i++){
            result.push(matrix[i][right])
            count--
        }
        
        for(let i = right; i > left; i--){
            result.push(matrix[bottom][i])
            count--
        }
        
        for(let i = bottom; i > top; i--){
            result.push(matrix[i][left])
            count--
        }
        
        top++
        left++
        bottom--
        right--
    }
    
    return result
};