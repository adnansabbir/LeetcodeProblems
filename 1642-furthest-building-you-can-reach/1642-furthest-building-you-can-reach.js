/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */


class MaxHeap{
    constructor(){
        this.values = []
    }
    
    push(value, priority){
        let contain = false
        for(let i = 0; i < this.values.length; i++){
            if(this.values[i] <= value){
                this.values.splice(i, 0, value)
                contain = true
                break
            }
        }
        if(!contain){
            this.values.push(value)
        }
    }
    pop(){
        if(this.isEmpty()) return null
        return this.values.shift()
    }
    front(){
        if(this.isEmpty()) return null
        return this.values[0]
    }
    isEmpty(){
        return this.values.length === 0
    }
    
    get(){
        return this.values
    }
}

var furthestBuilding = function(heights, bricks, ladders) {
    const maxHeap = new MaxHeap()
    let ans = 0
    for(let i = 1; i < heights.length; i++){
        const height = heights[i] - heights[i - 1]
        if(height > bricks) break
        if(height > 0){
            bricks -= height
            maxHeap.push(height)
        }
        ans++
    }
    
    let currIdx = ans + 1
    while(currIdx < heights.length){
        const height = heights[currIdx] - heights[currIdx - 1]
        
        if(height <= 0){
            ans++
        }else if(height <= bricks){
            bricks -= height
            maxHeap.push(height)
            ans++
        }else if(!maxHeap.isEmpty() && height < maxHeap.front() && ladders){
            bricks += maxHeap.pop() - height
            ladders--
            maxHeap.push(height)
            ans++
        }else if(ladders){
            ladders--
            ans++
        }else{
            break
        }
        
        currIdx++
    }
    console.log(bricks, ladders)
    return ans
    
};