function pacificAtlantic(heights: number[][]): number[][] {
    // null -> unchecked
    // -1 -> noFlow
    // 0 -> checking
    // 1 -> pacific ocean
    // 2 -> atlantic ocean
    // 3 -> both
    
    const H = heights.length
    const W = heights[0].length
    const flow = new Array<number[]>(H).fill([]).map(_ => new Array<number>(W))
    
    const getConnectedOcean = (h: number, w: number): number => {
        if(h<0 || w<0) return 1
        if(h>=H || w>=W) return 2
        return 0
    }
    
    const calculateFlow = (h: number, w:number): number => {
        if(flow[h][w] !== undefined) return flow[h][w]
        flow[h][w] = 0
        const oceans = new Set<number>()
        
        const neighbors = [[h-1, w], [h+1, w], [h,w-1], [h,w+1]].filter(([nh, nw]) => getConnectedOcean(nh,nw) || heights[h][w] >= heights[nh][nw])
        neighbors.forEach(([nh, nw]) => {
            if(getConnectedOcean(nh, nw) === 0 && heights[h][w] >= heights[nh][nw]) oceans.add(calculateFlow(nh, nw))
            else oceans.add(getConnectedOcean(nh, nw))
        })
        // console.log(h,w, oceans)
        
        if(oceans.has(3) || (oceans.has(2) && oceans.has(1))) flow[h][w] = 3
        else if(oceans.has(2)) flow[h][w] = 2
        else if(oceans.has(1)) flow[h][w] = 1
        
        if(oceans.has(0) && flow[h][w] !== 3){
            const result = flow[h][w]
            flow[h][w] = undefined
            return result
        }
        
        return flow[h][w]
    }
    
//     [[5,5,5,5],
//      [5,1,1,5],
//      [5,1,5,5],
//      [5,5,5,5]
//     ]
    
    const result = []
    for(let height = 0; height < H; height++){
        for(let width = 0; width < W; width++){
            calculateFlow(height, width)
            if(flow[height][width] === 3) result.push([height, width])
        }
    }
    // console.log(flow)
    return result
};