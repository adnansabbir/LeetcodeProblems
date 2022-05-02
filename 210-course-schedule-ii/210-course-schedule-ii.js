/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */

class Graph{
    constructor(size){
        this.vertexes = {}
        this.size = size
        for(let i = 0; i < size; i++){
            this.vertexes[i] = []
        }
    }
    
    addEdge(u, v){
        this.vertexes[u].push(v)
    }
    
    topSortUtil(u, visited, pending, stack){
        pending[u] = true
        
        for(let v of this.vertexes[u]){
            if(pending[v]) return false
            if(!visited[v] && !this.topSortUtil(v, visited, pending, stack)) return false
        }
        
        pending[u] = false
        visited[u] = true
        stack.push(u)
        
        return true
    }
    
    topSort(){
        const visited = Array(this.size).fill(false)
        const pending = Array(this.size).fill(false)
        const stack = []
        
        for(let i = 0; i < this.size; i++){
            if(!visited[i]){
                if(!this.topSortUtil(i, visited, pending, stack)){
                    return []
                }
            }
        }
        
        return stack
    }
}

var findOrder = function(numCourses, prerequisites) {
    const graph = new Graph(numCourses)
    prerequisites.forEach(pre => graph.addEdge(pre[0], pre[1]))
    return graph.topSort()
    // console.log(graph.vertexes)
    
};