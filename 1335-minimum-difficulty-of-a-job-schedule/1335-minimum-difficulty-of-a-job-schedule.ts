function minDifficulty(jobDifficulty: number[], d: number): number {
    const inf = Number.MAX_SAFE_INTEGER
    
    const memo = {}
    
    const dp = (idx: number, d: number, curr: number) => {
        const key = `${idx}-${d}-${curr}`
        if(memo[key] !== undefined) return memo[key]
        if(idx === jobDifficulty.length && d === 0) return curr
        if(idx >= jobDifficulty.length || d <= 0) return inf
        
        memo[key] =  Math.min(
            dp(idx+1, d, Math.max(curr, jobDifficulty[idx])),
            Math.max(curr, jobDifficulty[idx]) + dp(idx+1,d-1,0)
        )
        
        return memo[key]
    }
    
    const ans = dp(0,d,0)
    return ans === inf ? -1 : ans
};