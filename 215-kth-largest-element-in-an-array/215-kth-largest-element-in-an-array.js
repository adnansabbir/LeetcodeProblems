/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

class MaxHeap{
    constructor(size){
        this.nums = []
        this.size = size
    }
    
    push(item){
        let contains = false
        for(let i = 0; i < this.nums.length; i++){
            if(this.nums[i] <= item){
                this.nums.splice(i, 0, item)
                contains = true
                break
            }
        }
        
        if(!contains) this.nums.push(item)
        this.resize()
    }
    
    resize(){
        if(this.nums.length > this.size){
            this.nums.pop()
        }
    }
    
    getLast(){
        if(!this.nums.length) return
        return this.nums.at(-1)
    }
}

var findKthLargest = function(nums, k) {
    const maxHeap = new MaxHeap(k)
    
    nums.forEach(num => maxHeap.push(num))
    
    return maxHeap.getLast()
};