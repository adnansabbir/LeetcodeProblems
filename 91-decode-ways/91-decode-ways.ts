function numDecodings(s: string): number {
    if(s[0]==='0') return 0
    
    const dp = new Array<number>(s.length).fill(0)
    dp[0] = 1
    
    for(let i = 1; i < s.length; i++){
        if(s[i] !== '0'){
            dp[i] = dp[i-1]
        }

        const biggerCharAscii = parseInt(s[i-1] + s[i])
        const canFormLargerChar = biggerCharAscii>=10 && biggerCharAscii<=26
        if(canFormLargerChar){
            dp[i] += i >= 2 ? dp[i-2] : 1
        }

        if(dp[i] === 0){
            return 0
        }
    }
    
    
    // console.log(dp)
    return dp[dp.length-1]
};