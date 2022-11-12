class PQ{
    public queue: number[]
    constructor(){
        this.queue = []
    }

    private swapItems(idx1: number, idx2: number){
        const temp = this.queue[idx1]
        this.queue[idx1] = this.queue[idx2]
        this.queue[idx2] = temp
    }

    enqueue(value: number){
        this.queue.push(value)
        let cIdx = this.size() - 1
        while(cIdx !== 0){
            const pIndx = Math.floor((cIdx - 1) / 2)
            if(this.queue[cIdx] < this.queue[pIndx]){
                this.swapItems(cIdx, pIndx)
                cIdx = pIndx
            }else break
        }
    }

    dequeue(): number {
        if(this.size() === 1) return this.queue.pop()

        this.swapItems(0, this.size() - 1)
        const result = this.queue.pop()

        let cIdx = 0
        while(cIdx < this.size() - 1){
            const leftChildIdx = (cIdx * 2) + 1
            const rightChildIdx = (cIdx * 2) + 2
            let swapIdx = null

            if(leftChildIdx < this.size() && this.queue[leftChildIdx] < this.queue[cIdx]){
                swapIdx = leftChildIdx
            }

            if(rightChildIdx < this.size() &&
                ((swapIdx === null && this.queue[rightChildIdx] < this.queue[cIdx]) ||
                    (swapIdx !== null && this.queue[rightChildIdx] < this.queue[leftChildIdx]))
            ){
                swapIdx = rightChildIdx
            }

            if(swapIdx === null) break

            this.swapItems(cIdx, swapIdx)
            cIdx = swapIdx
        }

        return result
    }

    size(): number{
        return this.queue.length
    }
}

class MedianFinder {
    private minHeap: PQ
    private maxHeap: PQ
    constructor() {
        this.minHeap = new PQ()
        this.maxHeap = new PQ()
    }

    addNum(num: number): void {
        this.maxHeap.enqueue(num)

        if(this.maxHeap.size() > this.minHeap.size() + 1){
            this.minHeap.enqueue(-this.maxHeap.dequeue())
        }

        if(this.minHeap.size() && -this.minHeap.queue[0] > this.maxHeap.queue[0]){
            const temp = -this.minHeap.dequeue()
            this.minHeap.enqueue(-this.maxHeap.dequeue())
            this.maxHeap.enqueue(temp)
        }
        // console.log(this.minHeap.queue, this.maxHeap.queue)
    }

    findMedian(): number {
        // console.log(this.minHeap.queue, this.maxHeap.queue)
        if((this.maxHeap.size() + this.minHeap.size()) % 2 === 0){
            return (this.maxHeap.queue[0] - this.minHeap.queue[0]) / 2
        }
        else return this.maxHeap.queue[0]
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */