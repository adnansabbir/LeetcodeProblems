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
 * @return {number}
 */
var minCameraCover = function(root) {
    const coverage = new Set()
    coverage.add(null)
    let totalCam = 0
    
    const dfs = (node, parent) => {
        if(node === null) return
        const {right, left} = node
        dfs(right, node)
        dfs(left, node)

        if((!parent && !coverage.has(node)) || !coverage.has(right) || !coverage.has(left)){
            totalCam++
            coverage.add(node)
            coverage.add(parent)
            coverage.add(right)
            coverage.add(left)
        }
    }
    
    dfs(root, null)
    
    return totalCam
};