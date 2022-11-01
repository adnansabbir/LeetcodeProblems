function findBall(grid: number[][]): number[] {
    const M = grid.length, N = grid[0].length
    // 2 = yes
    // 3 = No
    const result = new Array<number[]>(M).fill([]).map(_ => new Array<number>(N))
    
    const getBottomIndex = (i: number, j: number): number => {
        if(i === M) return j
        if(result[i][j] !== undefined) return result[i][j]
        
        if((grid[i][j] === -1 && j=== 0) || (grid[i][j] === 1 && j=== N-1)){
            result[i][j] = -1
            return -1
        }
        
        let ans = -1
        
        if(grid[i][j] === 1 && grid[i][j] === grid[i][j+1]) ans = getBottomIndex(i+1, j+1)
        if(grid[i][j] === -1 && grid[i][j] === grid[i][j-1]) ans = getBottomIndex(i+1, j-1)
        
        result[i][j] = ans
        return ans
    } 
    
    for(let j = 0; j<N; j++){
        getBottomIndex(0, j)
    }
    
    return result[0]
    
    // from left to right
    // if leftmost is -1 it's blocked
    // if rightmost is 1 its blocked
    // if i + 1 on same direction ball can pass
};