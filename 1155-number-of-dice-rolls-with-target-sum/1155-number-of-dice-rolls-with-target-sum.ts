function numRollsToTarget(n: number, k: number, target: number): number {
//     1   2   3   4   5   6
//     1   2   3   4   5   6
    
//     target is - 3
    
//     start from -> target - ((n - 1) * k)
//     end at -> max(k, target - (n-1))
    
    if(target > n*k || target < n) return 0
    
    const MOD = 10**9 + 7
    const cache: Record<string, number> = {}
    const getCombination = (n: number, target: number) =>{
        
        const key = `${n}-${target}`
        if(cache[key] !== undefined){
            return cache[key]
        }
        
        if(target <= k && n==1) return 1
        
        const start = Math.max(1, target - ((n-1) * k))
        const end = target - (n-1) > k ? k : target - (n-1)
        
        let totalCombination = 0
        for(let i = start; i<=end; i++){
            totalCombination += getCombination(n-1, target - i)
        }
        totalCombination = totalCombination%MOD
        cache[key] = totalCombination
        return totalCombination
    }
    
    return getCombination(n, target)
    
}