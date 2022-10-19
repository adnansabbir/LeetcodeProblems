function largestIsland(grid: number[][]): number {
    const N = grid.length
    
    const getNeighbors = (r: number, c: number): number[][] => {
        const neighbors = []
        for(let [nr, nc] of [[r-1, c], [r+1, c], [r,c-1], [r, c+1]]){
            if(nr >= 0 && nr < N && nc >= 0 && nc < N) neighbors.push([nr, nc])
        }
        return neighbors
    }
    
    const dfs = (r: number, c: number, groupNo: number): number => {
        let size = 1
        grid[r][c] = groupNo
        for(let [nr, nc] of getNeighbors(r, c)){
            if(grid[nr][nc] === 1){
                size+= dfs(nr, nc, groupNo)
            }
        }
        
        return size
    } 
    
    const area: Record<number, number> = {}
    let groupCounter = 2
    for(let i = 0; i < N; i++){
        for(let j=0; j<N; j++){
            if(grid[i][j] !== 1) continue
            area[groupCounter] = dfs(i, j, groupCounter)
            groupCounter++
        }
    }
    
    let ans = Math.max(...Object.values(area), 1)
    for(let i = 0; i < N; i++){
        for(let j=0; j<N; j++){
            if(grid[i][j] !== 0) continue
            const neighborIds = getNeighbors(i, j).filter(([nr, nc]) => grid[nr][nc] > 1).map(([nr, nc]) => grid[nr][nc])
            const uniqueNeiborIds = Array.from(new Set(neighborIds))
            const sumOfNeighborAreas = uniqueNeiborIds.reduce((a, areaId)=> a + area[areaId], 0)
            ans = Math.max(ans, 1 + sumOfNeighborAreas)
        }
    }

    return ans
};