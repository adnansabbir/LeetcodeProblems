/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 Do not return anything, modify it in-place instead.
 */
function deleteNode(root: ListNode | null): void {
    let currentNode = root
    let prevNode = null
    while(currentNode && currentNode.next && currentNode.next.next){
        currentNode.val = currentNode.next.val
        currentNode = currentNode.next
    }

    currentNode.val = currentNode.next.val
    currentNode.next = null
};