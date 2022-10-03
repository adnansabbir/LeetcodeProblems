function minCost(colors: string, neededTime: number[]): number {
    // "a   a   a   a   b   b   b   a   b   b   b   b"
    // [5,  3,  3,  5,  7,  5,  3,  5,  5,  4,  8,  1]
    //                                  l   r
    // mintime = 19
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