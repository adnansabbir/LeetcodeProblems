/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
var criticalConnections = function(n, connections) {
    const result = []
    const disc = new Array(n)
    const low = new Array(n)
    const parents = new Array(n)
    let time = 0
    
    const adjs = {}
    connections.forEach(([u,v]) => {
        if(!(u in adjs)) adjs[u] = []
        if(!(v in adjs)) adjs[v] = []
        
        adjs[v].push(u)
        adjs[u].push(v)
    })
    
    const iterateWithTarjan = (node, parent) => {
        parents[node] = parent
        disc[node] = time
        low[node] = time
        time++
        
        for(let adj of adjs[node]){
            if(adj === parent) continue
            
            // Check if previously visited
            if(disc[adj] !== undefined){
                low[node] = Math.min(disc[adj], low[node])
                continue
            }
            
            iterateWithTarjan(adj, node)
            low[node] = Math.min(low[adj], low[node])
            
            if(disc[node] < low[adj]){
                result.push([node, adj])
            }
        }
    }
    
    iterateWithTarjan(0, -1)
    return result
};