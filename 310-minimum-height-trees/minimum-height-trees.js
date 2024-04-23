/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function(n, edges) {
    if(n === 1) return [0]
    if(n === 2) return [0,1]
    
    const neighbours = Array(n)
    for(let i = 0; i < n; i++){
        neighbours[i] = new Set()
    }
    
    edges.forEach(([u,v])=> {
        neighbours[u].add(v)
        neighbours[v].add(u)
    })
    
    let leaves = []
    for(let i = 0; i < n; i++){
        if(neighbours[i].size === 1){
            leaves.push(i)
        }
    }
    
    let remaining_nodes = n

    
    while(remaining_nodes > 2){
        remaining_nodes -= leaves.length
        const new_leaves = []
        
        while(leaves.length){
            const leaf = leaves.pop()
            neighbours[leaf].forEach(v => {
                neighbours[v].delete(leaf)
                if(neighbours[v].size === 1){
                    new_leaves.push(v)
                }
            })
            neighbours[leaf] = new Set()
        }
        
        leaves = new_leaves
    }
    
    return leaves
}