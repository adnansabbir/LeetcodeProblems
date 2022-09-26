function equationsPossible(equations: string[]): boolean {
    const graph: Record<string, Record<string, boolean>> = {}
    
    const canReach = (x: string, y: string, visisted = new Set<string>()): boolean => {
        if(Object.keys(graph[y]).length === 0) return false
        
        if(x === y) return true
        visisted.add(x)
        const neighboursOfX = Object.keys(graph[x]).filter(key => !visisted.has(key) && graph[x][key])
        return neighboursOfX.some(neighbour => canReach(neighbour, y, visisted))
    }
    
    equations.forEach(eq => {
        const x = eq[0]
        const y = eq[3]
        if(graph[x] === undefined) graph[x] = {}
        if(graph[y] === undefined) graph[y] = {}
        
        if(eq[1] === '='){
            graph[x][y] = true
            graph[y][x] = true   
        }
    })
    
    for(let eq of equations){
        if(eq[1] !== '!') continue
        const x = eq[0]
        const y = eq[3]
       
        if(x === y) return false
        
        if(canReach(x, y)) return false
        graph[x][y] = false
        graph[y][x] = false
    }
    
    
    return true
};