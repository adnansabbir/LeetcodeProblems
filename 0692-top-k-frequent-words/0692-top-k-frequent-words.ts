interface PriorityElement{
    word: string
    priority: number
}

//         1
//     2       3
//    4 5     6 

// [1234560]

class PriorityQueue{
    public items:PriorityElement[]
    
    constructor(){
        this.items = [] 
    }

    isSmaller(a: PriorityElement, b:PriorityElement){
        if(a.priority === b.priority) return a.word > b.word
        return a.priority < b.priority
    }

    swapItem(idx1: number, idx2: number){
        const idx1Temp = this.items[idx1]
        this.items[idx1] = this.items[idx2]
        this.items[idx2] = idx1Temp
    }

    push(word: string, priority: number){
        const item: PriorityElement = {word, priority}
        this.items.push(item)
        let curr = this.items.length - 1
        
        while(curr !== 0){
            const parent = Math.floor((curr - 1)/2)
            if(this.isSmaller(this.items[curr], this.items[parent])){
                this.swapItem(curr, parent)
                curr = parent
            }else{
                break
            }
        }
    }

    pop(){
        if(this.items.length === 1) return this.items.pop().word
        this.swapItem(0, this.items.length - 1)
        const item = this.items.pop()
        
        let curr = 0
        while(true){
            const leftChildIdx = (curr * 2) + 1
            const rightChildIdx = (curr * 2) + 2
            
            let swapIndex = null
            if(leftChildIdx < this.items.length && this.isSmaller(this.items[leftChildIdx], this.items[curr])){
                swapIndex = leftChildIdx
            }
            
            if(rightChildIdx < this.items.length && (
                (swapIndex === null && this.isSmaller(this.items[rightChildIdx], this.items[curr])) ||
               (swapIndex !== null && this.isSmaller(this.items[rightChildIdx], this.items[leftChildIdx]))
            )){
                swapIndex = rightChildIdx
            }
            
            if(swapIndex === null) return item.word
            
            this.swapItem(curr, swapIndex)
            curr = swapIndex
        }
        
        return item.word
    }

    isEmpty(){
        return this.items.length === 0
    }

    size(){
        return this.items.length
    }
}

function topKFrequent(words: string[], k: number): string[] {
    const pq = new PriorityQueue()
    const wordFreq = {}
    
    for(let word of words){
        wordFreq[word] = (wordFreq[word] || 0) + 1
    }
    Object.keys(wordFreq).forEach(key => {
        pq.push(key, wordFreq[key])
        if(pq.size() > k) pq.pop()
    })
    
    const result = []
    while(!pq.isEmpty()){
        result.push(pq.pop())
    }
    return result.reverse()
};