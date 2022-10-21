function pacificAtlantic(heights: number[][]): number[][] {
    // undefined -> unchecked
    // 0 -> no flow
    // 1 -> pacific ocean
    // 2 -> atlantic ocean
    // 3 -> both
    
    const R = heights.length
    const C = heights[0].length
    const flow = new Array<number[]>(R).fill([]).map(_ => new Array<number>(C))
    
    const setValue = (r: number, c: number, ocean: number) => {
        if(flow[r][c] === 3) return
        else if(flow[r][c] === undefined) flow[r][c] = ocean
        else if(flow[r][c] + ocean === 3) flow[r][c] = 3
    }
    
    const getNeighborsGreaterOrEqual = (r: number, c: number) => {
        const neighbors = [[r-1,c], [r+1,c],[r,c-1],[r,c+1]].filter(([nr,nc]) => !(nr<0 || nc<0 || nr>=R || nc>=C))
        return neighbors.filter(([nr,nc]) => heights[r][c] <= heights[nr][nc])
    }

    let queue: number[][] = []
    const connectOceans = (q: number[][], ocean: number) => {
        const visited = new Set<string>()
        while(q.length){
            const size = q.length
            for(let i = 0; i<size; i++){
                const [nr, nc] = q.shift()
                setValue(nr, nc, ocean)
                visited.add(`${nr}-${nc}`)
                const neighbors = getNeighborsGreaterOrEqual(nr,nc).filter(([r,c]) => !visited.has(`${r}-${c}`))
                q.push(...neighbors)
            }
        }
    }

    // putting pacific and atlantic to left and right column
    for(let r = 0; r<R; r++){
        for(let c = 0; c<C; c++){
            if(r===0 || c===0){
                queue.push([r,c])
            }
        }
    }
    connectOceans(queue, 1)

    queue = []
    // putting pacific and atlantic to top and bottom
    for(let r = 0; r<R; r++){
        for(let c = 0; c<C; c++){
            if(r+1===R || c+1===C){
                queue.push([r,c])
            }
        }
    }
    connectOceans(queue, 2)
    
    const result = []
    for(let r = 0; r<R; r++){
        for(let c = 0; c<C; c++){
            if(flow[r][c] === 3){
                result.push([r,c])
            }
        }
    }

    return result
};