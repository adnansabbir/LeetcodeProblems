var isBipartite = function (graph) {
  const visited = new Set()
  const group = {}
  
    const checkBipartite = (edge)=> {
        const stack = [edge]
        group[edge] = 'red'

        while(stack.length){
            const stackSize = stack.length
            for(let i = 0; i < stackSize; i++){
                const currEdge = stack.pop()
                visited.add(currEdge)
                const alternateColor = group[currEdge] === 'red' ? 'blue' : 'red'
                
                for(let adj of graph[currEdge]){
                    if(group[adj] === group[currEdge]) return false
                    if(group[adj] === alternateColor) continue
                    group[adj] = alternateColor
                    stack.push(adj)
                }   
            }
        }
        
        return true
    }
  
  for(let i = 0; i < graph.length; i++){
      if(!visited.has(i) && !checkBipartite(i)){
          return false
      }
  }
    
    return true
};