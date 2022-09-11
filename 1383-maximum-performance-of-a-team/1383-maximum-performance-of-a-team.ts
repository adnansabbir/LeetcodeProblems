function maxPerformance(n: number, speed: number[], efficiency: number[], k: number): number {
    const engineers = speed.map((s, i)=> [efficiency[i], s]).sort((p1,p2)=> p2[0]-p1[0])
    const pq = new MinPriorityQueue()
    
    let totalSpeed = 0
    let result = BigInt(0)
    const MOD = BigInt(10**9 + 7)
    
    for(let [eff, spd] of engineers){
        if(pq.size() === k){
            totalSpeed -= pq.dequeue().priority
        }
        
        pq.enqueue(spd, spd)
        totalSpeed += spd
        const currentPerformance = BigInt(eff) * BigInt(totalSpeed)
        if(currentPerformance > result) result = currentPerformance
    }
    return Number(result % MOD)
};