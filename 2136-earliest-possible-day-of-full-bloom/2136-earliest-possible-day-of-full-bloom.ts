function earliestFullBloom(plantTime: number[], growTime: number[]): number {
    const sortedGrowTimeIndices = growTime.map((_, i) => i).sort((i, j) => growTime[j] - growTime[i])
    let result = 0
    let pantingTime = 0
    let currentTotalTime = 0
    for(let i of sortedGrowTimeIndices){
        const currentTime = pantingTime + plantTime[i] + growTime[i]
        pantingTime += plantTime[i]
        if(currentTotalTime >= currentTime) continue
        currentTotalTime = currentTime
    }
    
    return currentTotalTime
};