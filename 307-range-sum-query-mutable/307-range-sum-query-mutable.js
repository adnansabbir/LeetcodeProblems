/**
 * @param {number[]} nums
 */

class NumArray{
    constructor(nums){
        this.cs = [0]
        for(let i = 0; i < nums.length; i++){
            this.cs.push(nums[i] + this.cs[i])
        }
        
        // console.log('create', this.cs)
    }
    
    update(index, val){
        const diff = val - this.sumRange(index, index)
        for(let i = index+1; i < this.cs.length; i++){
            this.cs[i] += diff
        }
        // console.log('update', this.cs)
    }
    
    sumRange(left, right){
        return this.cs[right+1]-this.cs[left]
        // console.log('sumRange', this.cs)
    }
}

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */