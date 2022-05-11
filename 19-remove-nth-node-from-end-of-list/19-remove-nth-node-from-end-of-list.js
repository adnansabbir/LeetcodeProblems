/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    const tempHead = new ListNode(0, head)
    let r = tempHead
    let l = tempHead
    
    
    for(let i = 0; i < n; i++){
        r = r.next
    }
    
    while(r.next){
        r = r.next
        l = l.next
    }
    
    l.next = l.next.next
    
    return tempHead.next
};