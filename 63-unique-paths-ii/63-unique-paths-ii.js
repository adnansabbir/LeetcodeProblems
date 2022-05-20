var uniquePathsWithObstacles = function(obstacleGrid) {
	// Edge case check -> If start or destination is blocked, we return 0
    if(obstacleGrid[0][0] === 1 || obstacleGrid.at(-1).at(-1) === 1) return 0
    
	// 1. Think in the reverse order
	// 2. The number of ways we can go from obstacleGrid[0][0] to obstacleGrid[n][n] 
	//    is the same as the number of ways we can go from obstacleGrid[n][n] to obstacleGrid[0][0]
	// 3. For reverse order instead of going right and bottom, we will go left, top
	// 4. Number of ways we can reach from  obstacleGrid[x][y] is via it's left(obstacleGrid[x][y-1]) and top(obstacleGrid[x-1][y]) 
	// 5. obstacleGrid[x][y] = obstacleGrid[x][y-1] + obstacleGrid[x-1][y]
	
    for(let i = 0; i < obstacleGrid.length; i++){
        for(let j = 0; j < obstacleGrid[0].length; j++){
			// if obstacleGrid[i][j] is 1, means we have an obstacle and we mark it as -1 which will help us to avoid it later
            obstacleGrid[i][j] = obstacleGrid[i][j] ? -1 : 0
            
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