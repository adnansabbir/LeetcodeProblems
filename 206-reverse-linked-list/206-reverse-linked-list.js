/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(!head) return head
    
    let tempHead = head
    let nextNode = head.next
    let prevNode = null
    
    while(nextNode){
        tempHead.next = prevNode
        prevNode = tempHead
        tempHead = nextNode
        nextNode = tempHead.next
    }
    
    tempHead.next = prevNode
    return tempHead
};