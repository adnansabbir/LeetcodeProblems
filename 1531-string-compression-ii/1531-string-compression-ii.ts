function getLengthOfOptimalCompression(s: string, k: number): number {
    const memo = {}
    const dfs = (cur, k, last, same) => {
        if (k < 0) return 101
        else if(len - cur === k) return 0
        const key = `${cur}_${k}_${last}_${same}`
        if(memo[key]) return memo[key]
        if(s[cur] === last){
            const carry = [1, 9, 99].includes(same) ?  1 : 0
            memo[key] = carry + dfs(cur+1, k, last, same+1)
            return memo[key]
        }
        const remain = 1 + dfs(cur+1, k, s[cur], 1)
        const deleted = dfs(cur+1, k-1, last, same)
        memo[key] = Math.min(remain, deleted)
        return memo[key]
    }
    const len = s.length
    return dfs(0, k, undefined, 0)
};