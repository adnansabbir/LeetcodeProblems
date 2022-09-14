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

class Balance{
    public frequency: Record<number, number>;
    public unbalanced: number
    constructor(){
        this.frequency = {}
        this.unbalanced = 0
    }

    add(value: number){
        if(this.frequency[value] === undefined){
            this.frequency[value] = 1
            this.unbalanced++
        }else{
            this.unbalanced += this.frequency[value]%2 === 0 ? 1 : -1
            this.frequency[value]++
        }
    }

    remove(value: number){
        this.unbalanced += this.frequency[value]%2 === 0 ? 1 : -1
        this.frequency[value]--
    }

    canHavePalindrom():boolean{
        return this.unbalanced <= 1
    }
}

function pseudoPalindromicPaths (root: TreeNode | null): number {
    let result = 0
    const traverse = (node: TreeNode | null, balance: Balance) => {
        if(!node) return
        
        balance.add(node.val)
        if(node.right || node.left){
            traverse(node.left, balance)
            traverse(node.right, balance)
        }else if(balance.canHavePalindrom()){
            result++
        }
        balance.remove(node.val)
    }
    traverse(root, new Balance())
    return result
};