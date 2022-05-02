/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    const dependency_map = {}
    const takenCourses = new Set()
    let pendingCourses = new Set()
    const result = []
    
    for(let i = 0; i< numCourses; i++){
        dependency_map[i] = []
    }
    
    
    for(let pre of prerequisites){
        const [course, dep] = pre
        dependency_map[course].push(dep)
    }
    
    
    const takeCourse = (cid) => {
        if(takenCourses.has(cid)) return true
        if(pendingCourses.has(cid)) return false
        if(!dependency_map[cid].length){
            takenCourses.add(cid)
            result.push(cid)
            return true
        }
        
        pendingCourses.add(cid)
        
        const allDepTaken = dependency_map[cid].map(dep => {
            return takeCourse(dep)
        }).every(c => c)
        
        if(!allDepTaken) return false
        
        pendingCourses.delete(cid)
        takenCourses.add(cid)
        result.push(cid)

        return true
        
    }
    
    for(let i = 0; i< numCourses; i++){
        if(!takeCourse(i)) return []
    }
    
    return result
    
};