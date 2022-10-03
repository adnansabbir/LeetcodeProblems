function minCost(colors: string, neededTime: number[]): number {
    let left = 0, right = 1
    let minCost = 0
    
    while(right < colors.length){
        if(colors[left] !== colors[right]){
            left = right
        }else if(neededTime[right] < neededTime[left]){
            minCost+= neededTime[right]
        }else{
            minCost+= neededTime[left]
            left = right
        }
            
        right++
    }
    
    return minCost
};