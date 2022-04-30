/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    const edges = {}
    equations.forEach((eq, idx) => {
        if(edges[eq[0]] === undefined){
            edges[eq[0]] = {}
        }
        edges[eq[0]][eq[1]] = values[idx]
        
        if(edges[eq[1]] === undefined){
            edges[eq[1]] = {}
        }
        edges[eq[1]][eq[0]] = 1/values[idx]
    })
    
    let visited = new Set()
    const calculateEq = (start, target, result) => {
        if(start === target) return result
        if(visited.has(start)) return -1
        visited.add(start)
             
        for(let adj of Object.keys(edges[start])){
            const value = calculateEq(adj, target, result * edges[start][adj])
            if(value !== -1) return value;
        }
        
        return -1
    }
    
    
    const result = queries.map(query=> {
        const [dividend, divisor] = query
        if(edges[dividend] === undefined || edges[divisor] === undefined) return -1.0
        
        if(edges[dividend][divisor] !== undefined) return edges[dividend][divisor]
        
        visited.clear()
        return calculateEq(dividend, divisor, 1)
    })
    
    return result
};