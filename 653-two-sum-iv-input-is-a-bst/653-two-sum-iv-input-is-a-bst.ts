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

function findTarget(root: TreeNode | null, k: number): boolean {
    const visted = new Set<number>()
    
    const queue = [root]
    while(queue.length){
        const size = queue.length
        for(let i = 0; i<size; i++){
            const node = queue.shift()
            const target = k - node.val
            if(visted.has(target)) return true
            visted.add(node.val)
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
        }
    }
    
    return false
};