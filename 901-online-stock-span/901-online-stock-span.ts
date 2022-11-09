class StockSpanner {
    private priceSpans: Array<number[]>
    constructor() {
        this.priceSpans = []
    }

    next(price: number): number {
        const priceSpan = [price, 1]

        while(this.priceSpans.length && this.priceSpans[this.priceSpans.length-1][0] <= price){
            priceSpan[1]+=this.priceSpans.pop()[1]
        }

        this.priceSpans.push(priceSpan)
        return priceSpan[1]
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */