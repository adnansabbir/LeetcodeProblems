/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    const newMatrix = new Array(matrix[0].length).fill(0).map(_ => new Array(matrix.length))
    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            newMatrix[j][i] = matrix[i][j]
        }
    }
    
    return newMatrix
};