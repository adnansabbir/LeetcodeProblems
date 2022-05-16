/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {
    if(grid[0][0] || grid.at(-1).at(-1) ) return -1
    const m = grid.length
    const n = grid[0].length
    
    const getNeigbours = (x, y) => {
        const neighbors = [
            [x-1, y], 
            [x+1, y], 
            [x, y+1], 
            [x, y-1], 
            [x + 1, y+1], 
            [x - 1, y-1], 
            [x - 1, y+1],
            [x + 1, y-1]
        ]
        
        return neighbors.filter(([nx, ny]) => (nx >= 0 && nx < m) && (ny >= 0 && ny < n) && !grid[nx][ny])
    }
    
    const queue = [[0,0]]
    const dp = {'0-0':1}
    while(queue.length){
        const size = queue.length
        const parent = queue.shift()
        const key = `${parent[0]}-${parent[1]}`
        for(let adj of getNeigbours(parent[0], parent[1])){
            const adjKey = `${adj[0]}-${adj[1]}`
            if(dp[adjKey] === undefined || dp[adjKey] > dp[key] + 1){
                dp[adjKey] = dp[key] + 1
                queue.push(adj)
            }
        }
    }
    
    return dp[`${m-1}-${n-1}`] || -1
};