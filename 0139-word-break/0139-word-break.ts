function wordBreak(s: string, wordDict: string[]): boolean {
    // app le [a, app, l, e]
    
    const wordSets = new Set<string>(wordDict)
    
    const dp:Record<string, boolean> = {}
    const canFormWord = (str: string): boolean =>{
        if(dp[str] !== undefined) return dp[str]
        if(wordSets.has(str)) return true
        if(str.length === 1) return false
        
        for(let i = 1; i<str.length; i++){
            const left = str.substring(0,i)
            const right = str.substring(i)
            if(canFormWord(left) && canFormWord(right)) {
                dp[str] = true
                return true
            }
        }
        
        dp[str] = false
        return false
    }
    
    return canFormWord(s)
};