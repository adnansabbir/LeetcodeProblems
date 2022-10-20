function longestCommonSubsequence(text1: string, text2: string): number {
    const dp = new Array<number[]>(text1.length).fill([]).map(_ => new Array<number>(text2.length).fill(0))
    
    const getValue = (i: number, j:number) => i < 0 || j < 0 ? 0 : dp[i][j]
    for(let t1 = 0; t1 < dp.length; t1++){
        for(let t2 = 0; t2 < dp[0].length; t2++){
            if(text1[t1] === text2[t2]){
                dp[t1][t2] = 1 + getValue(t1-1,t2-1)
            }else{
                dp[t1][t2] = Math.max(getValue(t1-1,t2), getValue(t1,t2-1))
            }
        }
    }
    
    return dp[dp.length-1][dp[0].length-1]
};