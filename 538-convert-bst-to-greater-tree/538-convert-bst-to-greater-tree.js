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
    const toGreaterTree = (root, top, rightChild)=> {
        if(!root) return top
        
        root.val += top
        root.val += !!root.right ? toGreaterTree(root.right, top, true) : 0
        const result = !!root.left ? toGreaterTree(root.left, root.val, false) : root.val
        return !!rightChild ? result - top : result
    }
    
    toGreaterTree(root, 0)
    return root
};