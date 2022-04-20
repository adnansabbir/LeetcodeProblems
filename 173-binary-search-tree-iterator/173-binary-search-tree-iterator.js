/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 */
class BSTIterator{
    constructor(root){
        this.root = root
        this.values = []
        this.pos = 0
        this.createSortedArray(root)
        console.log(this.values)
    }
    
    createSortedArray(root){
        if(!root) return
        this.createSortedArray(root.left)
        this.values.push(root.val)
        this.createSortedArray(root.right)
    }
    
    next(){
        return this.values[this.pos++]
    }
    
    hasNext(){
        return this.pos<this.values.length
    }
}
// var BSTIterator = function(root) {
    
// };

// /**
//  * @return {number}
//  */
// BSTIterator.prototype.next = function() {
    
// };

// /**
//  * @return {boolean}
//  */
// BSTIterator.prototype.hasNext = function() {
    
// };

/** 
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */