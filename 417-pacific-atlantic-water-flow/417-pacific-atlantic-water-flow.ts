function pacificAtlantic(heights: number[][]): number[][] {
    const m = heights.length
    const n = heights[0].length
    const dp = new Array<number[]>(m).fill(null).map(d=> new Array<number>(n))
    dp[0][n-1] = 3
    dp[m-1][0] = 3
    
    // 1 == Pacific Ocean
    // 2 == Atlantic Ocean
    const getOcean = (x:number, y:number): number => {
        if (x<0 || y<0) return 1
        if (x>=m || y>=n) return 2
        return 0
    }
    
    
    const canReachBothOcean = (x:number, y:number):number => {
        if(dp[x][y] !== undefined) return dp[x][y]
        dp[x][y] = -1
        const oceans = new Set()
        
        if(getOcean(x-1,y) === 0 && heights[x-1][y]<= heights[x][y]){
            oceans.add(canReachBothOcean(x-1,y))
        }else oceans.add(getOcean(x-1,y))
        // if(x==1 && y==4) console.log(oceans)
        
        if(getOcean(x,y-1) === 0 && heights[x][y-1]<= heights[x][y]){
            oceans.add(canReachBothOcean(x,y-1))
        }else oceans.add(getOcean(x,y-1))
        // if(x==1 && y==4) console.log(oceans)
        
        if(getOcean(x+1,y) === 0 && heights[x+1][y]<= heights[x][y]){
            oceans.add(canReachBothOcean(x+1,y))
        }else oceans.add(getOcean(x+1,y))
        // if(x==1 && y==4) console.log(oceans)
        
        if(getOcean(x,y+1) === 0 && heights[x][y+1]<= heights[x][y]){
            oceans.add(canReachBothOcean(x,y+1))
        }else oceans.add(getOcean(x,y+1))
        
        // if(x==1 && y==4) console.log(oceans, heights[x][y+1], heights[x][y], getOcean(x,y+1))
        
        let result = 0
        if(oceans.has(3)) result = 3
        else if(oceans.has(1) && oceans.has(2)) result = 3
        else if(oceans.has(1)) result = 1
        else if(oceans.has(2)) result = 2
        
        
        if(oceans.has(-1) && result!==3){
            dp[x][y] = undefined
            return result
        }
        dp[x][y] = result
        return dp[x][y]
    }
    const result = []
    for(let i = 0; i < m; i++){
        for(let j = 0; j < n; j++){
            if(canReachBothOcean(i,j)===3){
                result.push([i,j])
            }
        }
    }
    return result
};