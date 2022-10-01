function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // creating the course dependencies
    const courseDependencies: Record<number, number[]> = {}
    prerequisites.forEach(([course, dependentCourse])=> {
        if(courseDependencies[course] === undefined){
            courseDependencies[course] = [dependentCourse]
        }else{
            courseDependencies[course].push(dependentCourse)
        }
    })
        
    const completedCourse = new Array<number>(numCourses).fill(-1)
    
    const canCompleteCourse = (courseNo: number) => {
        if(completedCourse[courseNo] === 0) return false
        if(completedCourse[courseNo] === 1) return true
        
        completedCourse[courseNo] = 0
        if(courseDependencies[courseNo] === undefined){
            completedCourse[courseNo] = 1
            return true
        }
        
        for(let dependency of courseDependencies[courseNo]){
            if(!canCompleteCourse(dependency)) return false
        }
        completedCourse[courseNo] = 1
        return true
    }
    
    for(let i = 0; i<numCourses; i++){
        if(!canCompleteCourse(i)) return false
    }
    
    return true
};