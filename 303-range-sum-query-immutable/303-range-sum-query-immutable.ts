class NumArray {
    public nums: number[]
    constructor(nums: number[]) {
        this.nums = nums
        for(let i = 1; i<this.nums.length; i++){
            this.nums[i] += this.nums[i-1]
        }
    }

    sumRange(left: number, right: number): number {
        return left ? this.nums[right] - this.nums[left-1] : this.nums[right]
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */