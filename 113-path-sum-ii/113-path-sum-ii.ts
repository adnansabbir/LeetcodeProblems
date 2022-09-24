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

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    if(!root) return []
    
    const result = []
    const traverse = (node: TreeNode|null, sum = 0, nodeValues = [])=> {
        if(!node) return
        
        sum+=node.val
        nodeValues.push(node.val)
        
        if(node.right || node.left){
            traverse(node.left, sum, nodeValues)
            traverse(node.right, sum, nodeValues)
        }else if(sum === targetSum){
            result.push([...nodeValues])
        }
        
        nodeValues.pop()
    }
    
    traverse(root)
    return result
};