function rob(nums: number[]): number {
    const findMaxMoney = (arr: number[]) => {
        if(arr.length <= 2) return Math.max(...arr)
        if(arr.length === 3) return Math.max(arr[0]+arr[2], arr[1])
        
        const dp = new Array<number>(arr.length).fill(0)
        dp[0] = arr[0]
        dp[1] = arr[1]
        dp[2] = arr[0] + arr[2]
        
        for(let i = 3; i<arr.length; i++){
            dp[i] = Math.max(arr[i] + dp[i-3], arr[i] + dp[i-2], dp[i-1])
        }
        
        return dp[arr.length-1]
    }
    
    const lastElem = nums.pop()
    const maxWithoutLast = findMaxMoney(nums)
    nums.shift()
    nums.push(lastElem)
    const maxWithoutFirst = findMaxMoney(nums)
    return Math.max(maxWithoutLast, maxWithoutFirst)
};