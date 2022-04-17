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
var increasingBST = function(root) {
    let newHead = null
    let tempHead = null
    
    const construct = (node)=> {
        if(!node) return
        construct(node.left)
        if(!tempHead){
            newHead = new TreeNode(node.val)
            tempHead = newHead
        }else{
            tempHead.right = new TreeNode(node.val)
            tempHead = tempHead.right
        }
        construct(node.right)
    }
    
    construct(root)
    return newHead
};