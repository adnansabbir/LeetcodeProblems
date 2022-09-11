class MinHeap{
    public values:Array<number>
    
    constructor(){
        this.values = []
    }
    
    push(value: number):void{
        this.values.push(value)
        
        let index = this.values.length - 1
        const current = this.values[index]
        
        while(index > 0){
            const parentIndex = Math.floor((index-1)/2)
            const parentValue = this.values[parentIndex]
            if(parentValue > current){
                this.values[parentIndex] = current
                this.values[index] = parentValue
                index = parentIndex
            }else break
        }
    }
    
    pop():number{
        if(this.values.length === 1) return this.values.pop()
        const minValue = this.values[0]
        const lastValue = this.values.pop()
        this.values[0] = lastValue
        
        let index = 0
        const length = this.values.length
        const current = this.values[0]
        while(true){
            const leftChildIndex = (2 * index) + 1
            const rightChildIndex = (2 * index) + 2
            let leftChild, righChild
            let swapIndex: number = null
            
            if(leftChildIndex < length){
                const leftChild = this.values[leftChildIndex]
                if(leftChild < current) swapIndex = leftChildIndex
            }
            
            if(rightChildIndex < length){
                const rightChild = this.values[rightChildIndex]
                if(
                    (swapIndex === null && rightChild < current) ||
                    (swapIndex !== null && rightChild < this.values[leftChildIndex])
                    ) swapIndex = rightChildIndex
            }
                
            if(swapIndex === null) break
            
            this.values[index] = this.values[swapIndex]
            this.values[swapIndex] = current
            index = swapIndex
        }
        return minValue
    }
    
    isEmpty():boolean{
        return this.values.length === 0
    }

    size():number{
        return this.values.length
    }
}

function maxPerformance(n: number, speed: number[], efficiency: number[], k: number): BigInt {
    const performance = speed.map((s, i)=> [efficiency[i], s]).sort((p1,p2)=> p2[0]-p1[0])
    const minHeap = new MinHeap()
    
    let maxPerformance = 0
    let totalSpeed = 0
    let result = BigInt(0)
    const MOD = BigInt(10**9 + 7)
    for(let [eff,spd] of performance){
        if(minHeap.size() === k){
            totalSpeed -= minHeap.pop()
        }
        
        totalSpeed += spd
        const currentPerformance = BigInt(eff) * BigInt(totalSpeed)
        if(currentPerformance > result) result = currentPerformance
        minHeap.push(spd)
    }
    return result % MOD
};