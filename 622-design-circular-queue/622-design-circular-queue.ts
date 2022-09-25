class MyCircularQueue {
    private queue: Array<number>;
    private start: number
    private end: number
    private size: number
    
    constructor(k: number) {
        this.queue = new Array<number>(k)
        this.start = 0
        this.end = -1
        this.size = k
    }

    enQueue(value: number): boolean {
        if(this.isFull()) return false
        this.end = (this.end + 1) % this.size
        this.queue[this.end] = value
        return true
    }

    deQueue(): boolean {
        if(this.isEmpty()) return false
        
        if(this.start === this.end){
            this.start = 0
            this.end = -1
            return true
        }
        
        this.start = (this.start + 1) % this.size
        return true
    }

    Front(): number {
        if(this.isEmpty()) return -1
        return this.queue[this.start]
    }

    Rear(): number {
        if(this.isEmpty()) return -1
        return this.queue[this.end]
    }

    isEmpty(): boolean {
        return this.end === -1
    }

    isFull(): boolean {
        return !this.isEmpty() && (this.end + 1) % this.size === this.start
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */