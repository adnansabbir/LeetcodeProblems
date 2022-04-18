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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    const smaller = [0]
    const findKth = (root)=> {
        if(!root) return null
        findKth(root.left)
        smaller.push(root.val)
        findKth(root.right)
    }
    
    findKth(root)
    return smaller[k]
};