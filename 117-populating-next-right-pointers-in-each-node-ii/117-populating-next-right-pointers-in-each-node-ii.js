/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    if(!root) return root
    
    const queue = [root]
    
    while(queue.length){
        const n = queue.length
        let currNode = null
        
        for(let i = 0; i < n; i++){
            if(currNode === null){
                currNode = queue.shift()
            }else{
                currNode.next = queue.shift()
                currNode = currNode.next   
            }
            if(currNode.left) queue.push(currNode.left)
            if(currNode.right) queue.push(currNode.right)
        }
    }
    
    return root
};