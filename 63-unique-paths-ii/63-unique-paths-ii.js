/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    if(obstacleGrid[0][0] === 1 || obstacleGrid.at(-1).at(-1) === 1) return 0
    
    for(let i = 0; i < obstacleGrid.length; i++){
        for(let j = 0; j < obstacleGrid[0].length; j++){
            obstacleGrid[i][j] = obstacleGrid[i][j] ? obstacleGrid[i][j] * -1 : 0
            if(i === 0 && j === 0){
                obstacleGrid[i][j] = 1
            }
            else if (obstacleGrid[i][j] === 0){
                const left = j > 0 ? Math.max(obstacleGrid[i][j - 1], 0) : 0
                const top = i > 0 ? Math.max(obstacleGrid[i - 1][j], 0) : 0
                obstacleGrid[i][j] = left + top
            }
        }
    }
    
    return obstacleGrid.at(-1).at(-1)
};