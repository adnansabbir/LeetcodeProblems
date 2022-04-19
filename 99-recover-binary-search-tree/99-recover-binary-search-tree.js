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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    let first = null
    let second = null
    let prevNode = new TreeNode(Number.NEGATIVE_INFINITY)
    
    const inorder = (treeNode)=> {
        if(!treeNode) return
        
        inorder(treeNode.left)
        
        if(!first && prevNode.val > treeNode.val){
            first = prevNode
        }
        
        if (first && prevNode.val > treeNode.val){
            second = treeNode
        }
        
        prevNode = treeNode
        
        inorder(treeNode.right)
    }
    
    inorder(root)
    const temp = second.val
    second.val = first.val
    first.val = temp
};