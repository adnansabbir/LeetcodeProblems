/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    const headARef = new Set()
    let hA = headA
    let hB = headB
    
    while(hA){
        headARef.add(hA)
        hA = hA.next
    }
    
    while(hB){
        if(headARef.has(hB)) return hB
        hB = hB.next
    }
    
    return null
};