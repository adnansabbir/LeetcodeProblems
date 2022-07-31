class TreeNode{
    constructor(sum, start, end, left = null, right = null){
        this.sum = sum
        this.start = start
        this.end = end
        this.left = left
        this.right = right
    }
}
class NumArray{
    constructor(nums){
        this.tree = this.buildSegmentTree(0, nums.length-1, nums)
    }
    
    buildSegmentTree(start,end, nums){
        if(start === end) return new TreeNode(nums[start], start, end)
        const mid = parseInt((start + end) / 2)
        const left = this.buildSegmentTree(start, mid, nums)
        const right = this.buildSegmentTree(mid+1, end, nums)
        return new TreeNode(left.sum + right.sum, start, end, left, right)
    }
    
    update(index, val, tree = null){
        tree = tree || this.tree
        const mid = parseInt((tree.start + tree.end)/2)
        
        if(tree.start === tree.end){
            tree.sum = val
            return
        }else if(index <= mid){
            this.update(index, val, tree.left)
        }else{
            this.update(index, val, tree.right)
        }
        
        tree.sum = tree.left.sum + tree.right.sum
    }
    
    sumRange(start, end, tree = null){
        tree = tree || this.tree
        if(tree.start === start && tree.end === end) return tree.sum
        const mid = parseInt((tree.start + tree.end)/2)
        
        if(start <= mid && end<= mid){
            return this.sumRange(start, end, tree.left)
        }else if(start > mid && end > mid){
            return this.sumRange(start, end, tree.right)
        }else{
            return this.sumRange(start, mid, tree.left) + this.sumRange(mid+1, end, tree.right)
        }
    }
}

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */