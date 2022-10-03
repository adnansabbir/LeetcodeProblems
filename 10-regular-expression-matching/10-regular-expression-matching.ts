function isMatch(s: string, p: string): boolean {
    const cache: Record<string, boolean> = {}
    const dp = (i:number, j:number) => {
        const key = `${i}-${j}`
        if(cache[key] !== undefined) return cache[key]
        
        let ans = false
        if(j === p.length){
            ans = i === s.length
        }else{
            const firstElemMatched = i < s.length && [s[i], '.'].includes(p[j])
            
            if(j+1 < p.length && p[j+1] === '*'){
                ans = dp(i, j+2) || (firstElemMatched && dp(i+1, j)) 
            }else{
                ans = firstElemMatched && dp(i+1, j+1)
            }
        }
        
        cache[key] = ans
        return ans
    }

    return dp(0,0)    
};