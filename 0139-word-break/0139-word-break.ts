function wordBreak(s: string, wordDict: string[]): boolean {
    const dp = new Array<boolean>(s.length).fill(false)
    dp.push(true)
    
    for(let i = s.length - 1; i>=0; i--){
        for(let word of wordDict){
            if(s.substring(i).startsWith(word)){
                dp[i] = dp[i+word.length]
            }
            if(dp[i]) break
        }
    }
    console.log(dp)
    return dp[0]
};