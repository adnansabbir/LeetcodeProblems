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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    if(n === 0 || !head) return head
    
    const preHead = new ListNode(0, head)
    let nMinus1th = preHead
    let end = preHead
    
    while(end && n){
        end = end.next
        n--
    }
    
    while(end.next){
        end = end.next
        nMinus1th = nMinus1th.next
    }
    
    nMinus1th.next = nMinus1th.next.next
    return preHead.next
};