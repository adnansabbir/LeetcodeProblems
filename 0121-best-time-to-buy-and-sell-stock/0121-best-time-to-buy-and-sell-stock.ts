function maxProfit(prices: number[]): number {
    let profit = 0
    let lowestPrice = prices[0]
    for(let price of prices){
        if(price < lowestPrice){
            lowestPrice = price
        }else{
            profit = Math.max(profit, price - lowestPrice)
        }
    }
    
    return profit
};