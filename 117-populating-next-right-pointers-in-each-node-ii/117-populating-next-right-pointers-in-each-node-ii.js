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

const getLeftMostNext = (root) => {
    if(!root) return null
    
    if(root.left) return root.left
    if(root.right) return root.right
    return getLeftMostNext(root.next)
}

var connect = function(root, next = null) {
    if(!root) return root
    
    root.next = next
    
    const nextForRight = getLeftMostNext(next)
    connect(root.right, nextForRight)
    
    const nextForLeft = root.right || nextForRight
    
    connect(root.left, nextForLeft)
    
    return root
};