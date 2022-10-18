function canCompleteCircuit(gas: number[], cost: number[]): number {
    const getSum = (arr: number[]) => arr.reduce((a, c) => a + c, 0)
    
    if(getSum(gas) < getSum(cost)) return -1
    
    const size = gas.length
    
    let fuel = 0, start = 0
    for(let i = 0; i<size; i++){
        fuel += gas[i] - cost[i]
        if(fuel < 0){
            fuel = 0
            start = i+1
        }
    }
    
    return start
};