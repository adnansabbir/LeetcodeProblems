function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const graph = {}
    
    const isDependentOn = (course1: number, course2: number): boolean => {
        const visisted = new Set<number>()
        const queue = [course1]
        while(queue.length){
            const size = queue.length
            for(let i = 0; i<size; i++){
                const curr = queue.shift()
                visisted.add(curr)
                if(curr === course2) return true
                if(graph[curr] === undefined) continue
                queue.push(...graph[curr].filter(node => !visisted.has(node)))
            }
        }
        
        return false
    }
    
    
    for(let [course, dependent] of prerequisites){
        if(graph[course] == undefined){
            graph[course] = []
        }
        
        if(isDependentOn(dependent, course)) return false
        graph[course].push(dependent)
    }

    return true
};