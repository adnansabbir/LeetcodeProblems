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
    
    print(node, result = []){
        if(node.start === node.end){
            result.push(node.sum)
            return
        }
        
        this.print(node.left, result)
        this.print(node.right, result)
        return result
    }
    
    update(index, val, nodeHead = null){
        const node = nodeHead || this.tree
        const mid = parseInt((node.start + node.end)/2)
        
        if(node.start === node.end){
            node.sum = val
            return
        }else if(index <= mid){
            this.update(index, val, node.left)
        }else{
            this.update(index, val, node.right)
        }
        
        node.sum = node.left.sum + node.right.sum
    }
    
    sumRange(start, end, nodeHead = null){
        const node = nodeHead || this.tree
        if(node.start === start && node.end === end) return node.sum
        const mid = parseInt((node.start + node.end)/2)
        
        if(start <= mid && end<= mid){
            return this.sumRange(start, end, node.left)
        }else if(start > mid && end > mid){
            return this.sumRange(start, end, node.right)
        }else{
            return this.sumRange(start, mid, node.left) + this.sumRange(mid+1, end, node.right)
        }
    }
}

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */