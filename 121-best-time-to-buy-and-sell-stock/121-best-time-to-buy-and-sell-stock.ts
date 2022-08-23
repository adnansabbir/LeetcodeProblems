function maxProfit(prices: number[]): number {
    let minPrice = prices[0]
    let maxProfit = 0
    for(let price of prices){
        minPrice = Math.min(minPrice, price)
        maxProfit = Math.max(maxProfit, price - minPrice)
    }
    
    return maxProfit
};