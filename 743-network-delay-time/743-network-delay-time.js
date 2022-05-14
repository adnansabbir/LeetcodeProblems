/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
    const graph = {}
    times.forEach(([u,v,w])=> {
        if(!(u in graph)){
            graph[u] = []
        }
        graph[u].push({v,w})
    })
    
    if(!(k in graph)){
        return -1
    }
    
    const distanceFromSource = new Array(n+1).fill(Infinity)
    distanceFromSource[k] = 0
    const queue = [k]
    
    let max_distance = {v: null, w: -Infinity}
    
    while(queue.length){
        const size = queue.length
        const visited = new Set()
        for(let i = 0; i < size; i++){
            const currNodeVal = queue.shift()
            const currNode = graph[currNodeVal] || []
            if(visited.has(currNodeVal)) continue
            else visited.add(currNodeVal)
            
            currNode.forEach(({v,w})=> {
                const currentTime = Math.min(distanceFromSource[currNodeVal] + w, distanceFromSource[v])
                if(currentTime < distanceFromSource[v]){
                    queue.push(v)
                    distanceFromSource[v] = currentTime
                }
                if(distanceFromSource[v] > max_distance.w || max_distance.v === v){
                    max_distance = {v, w: distanceFromSource[v]}
                }
            })
        }
    }
    
    distanceFromSource.shift()
    if(distanceFromSource.some(v => v === Infinity)) return -1
    return max_distance.w
};