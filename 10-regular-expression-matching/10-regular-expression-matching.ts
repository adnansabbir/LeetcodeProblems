function isMatch(s: string, p: string): boolean {
    // s = 'acdd'
    // p = 'a.*d'
    
    
    const dp = (i:number, j:number) => {
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
        
        return ans
    }
    
    return dp(0,0)    
};