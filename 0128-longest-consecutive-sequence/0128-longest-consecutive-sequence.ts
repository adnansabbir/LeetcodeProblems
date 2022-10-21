function longestConsecutive(nums: number[]): number {
    const visited = {}
    for(let num of nums){
        visited[num] = false
    }
    

    let maxStreak = 0
    for(let num of nums){
        if(visited[num]) continue
        let streak = 1
        let currentNum = num+1
        while(visited[currentNum] !== undefined){
            visited[currentNum] = true
            streak++
            currentNum++
        }
        
        currentNum = num-1
        while(visited[currentNum] !== undefined){
            visited[currentNum] = true
            streak++
            currentNum--
        }
        
        maxStreak = Math.max(maxStreak, streak)
    }
    
    return maxStreak
};