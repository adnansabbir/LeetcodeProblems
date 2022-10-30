function shortestPath(grid: number[][], k: number): number {
    const M = grid.length, N = grid[0].length
    const queue = [[0,0,0,k]]
    const neighbors = [[-1,0], [1,0], [0,-1], [0,1]]
    const lives = new Array<number[]>(M).fill([]).map(_ => new Array<number>(N).fill(-1))
    
    while(queue.length){
        const size = queue.length
        for(let i = 0; i<size; i++){
            let [r, c, distance, l] = queue.shift()
            
            if(r === M-1 && c === N-1) return distance
            
            if(grid[r][c] === 1) l--
            
            for(let [x, y] of neighbors){
                const row = r+x, col = c+y
                if(row < 0 || row >= M || col < 0 || col >= N || lives[row][col] >= l) continue
                queue.push([row, col, distance+1, l])
                lives[row][col] = l
            }
        }
    }
    
    return -1
};