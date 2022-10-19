function maxProfit(prices: number[]): number {
    let buyingPrice = prices[0]
    let profit = 0
    for(let i = 1; i < prices.length; i++){
        if(prices[i] > buyingPrice){
            profit = Math.max(profit, prices[i] - buyingPrice)
        }else{
            buyingPrice = prices[i]
        }
    }
    
    return profit
};