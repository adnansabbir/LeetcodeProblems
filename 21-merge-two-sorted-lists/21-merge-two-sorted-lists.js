/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let l1 = list1
    let l2 = list2
    const tempHead = new ListNode()
    let pointer = tempHead
    
    while(l1 && l2){
        if(l1.val < l2.val){
            pointer.next = l1
            pointer = l1
            l1 = l1.next
        }else{
            pointer.next = l2
            pointer = l2
            l2 = l2.next
        }
    }
    
    if(l1){
        pointer.next = l1
    }else{
        pointer.next = l2
    }
    
    return tempHead.next
};