/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function addOneRow(root: TreeNode | null, val: number, depth: number): TreeNode | null {
    if(depth == 1) return new TreeNode(val, root)
    
    const nodesAtGivenDepth = [root]
    
    while(nodesAtGivenDepth.length){
        if(depth === 2) break
        const size = nodesAtGivenDepth.length
        for(let i = 0; i<size; i++){
            const node = nodesAtGivenDepth.shift()
            if(node.left) nodesAtGivenDepth.push(node.left)
            if(node.right) nodesAtGivenDepth.push(node.right)
        }
        depth--
    }
    
    // console.log(nodesAtGivenDepth)
    
    nodesAtGivenDepth.forEach(node => {
        node.left = new TreeNode(val, node.left)
        node.right = new TreeNode(val, null, node.right)
    })
    
    return root
};