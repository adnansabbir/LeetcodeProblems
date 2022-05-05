/**
 * @param {number[][]} matrix
 * @return {number}
 */

var longestIncreasingPath = function(matrix) {
    const pathMatrix = Array(matrix.length)
    matrix.forEach((row, i) => {
        pathMatrix[i] = Array(row.length)
    })
    
    const getSmallerNeighbours = (x, y, matrix) => {
        const neighbours = []
        const r = matrix.length
        const c = matrix[0].length
        
        if(x > 0 && matrix[x][y] > matrix[x-1][y]) neighbours.push([x-1, y])
        
        if(y > 0 && matrix[x][y] > matrix[x][y-1]) neighbours.push([x, y-1])
        
        if(x < r - 1 && matrix[x][y] > matrix[x+1][y]) neighbours.push([x+1, y])
        
        if(y < c - 1 && matrix[x][y] > matrix[x][y+1]) neighbours.push([x, y+1])
        
        return neighbours
    }
    
    
    const calculatePath = (x,y) => {
        if(pathMatrix[x][y] !== undefined) return pathMatrix[x][y]
        
        const neighbours = getSmallerNeighbours(x, y, matrix)
        if(!neighbours.length){
            pathMatrix[x][y] = 1
            return 1
        }
        
        let maxPath = 0
        neighbours.forEach(([x,y])=> {
            maxPath = Math.max(maxPath, calculatePath(x, y))
        })
        
        pathMatrix[x][y] = maxPath + 1
        
        return pathMatrix[x][y]
    }
    
    let maxPath = 0
    matrix.forEach((row, i) => {
        row.forEach((col, j) => {
            maxPath = Math.max(maxPath, calculatePath(i, j))
        })
    })
    
    return maxPath
};