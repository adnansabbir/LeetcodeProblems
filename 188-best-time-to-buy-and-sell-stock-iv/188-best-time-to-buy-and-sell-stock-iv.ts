function maxProfit(k: number, prices: number[]): number {
    if(k==0 || prices.length <= 1) return 0
    const dp = {}
    const getMaxProfit = (cidx: number, buying: boolean, transaction: number) => {
        if(transaction === 0 || cidx === prices.length) return 0
        const key = `(${cidx})(${buying})(${transaction})`
        if(dp[key]!== undefined) return dp[key]
        
        // skip
        let profit = getMaxProfit(cidx + 1, buying, transaction)
        
        if(buying){
            profit = Math.max(profit, getMaxProfit(cidx + 1, !buying, transaction) - prices[cidx])
        }else{
            profit = Math.max(profit, getMaxProfit(cidx + 1, !buying, transaction - 1) + prices[cidx])
        }
        
        dp[key] = profit
        return dp[key]
    }
    const result = getMaxProfit(0, true, k)
    return result
};