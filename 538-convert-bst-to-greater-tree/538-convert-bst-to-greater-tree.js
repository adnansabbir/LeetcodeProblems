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
 * @return {TreeNode}
 */
var convertBST = function(root) {
    let sum = 0
    const toGreaterTree = (root)=> {
        if(!root) return root
        
        toGreaterTree(root.right)
        sum+=root.val
        root.val = sum
        toGreaterTree(root.left)
        
        return root
    }
    
    return toGreaterTree(root)
};