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

function deleteMiddle(head: ListNode | null): ListNode | null {
    const preHead = new ListNode(null, head)
    let fast = preHead
    let slow = preHead
    
    while(fast && fast.next && fast.next.next){
        fast = fast.next.next
        slow = slow.next
    }
    
    slow.next = slow.next.next
    return preHead.next
};