/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if(!head.next || !head.next.next) return head
    
    const splitToHalf = (head) => {
        let slow = head
        let fast = head
        
        while(fast && fast.next){
            fast = fast.next.next
            if(fast){
                slow = slow.next
            }
        }
        const secondHalf = slow.next
        slow.next = null
        return [head, secondHalf]
    }
    
    
    const reverseList = (head) => {
        let newHead = head
        let nextNode = head.next
        let prevNode = null
        
        while(nextNode){
            newHead.next = prevNode
            prevNode = newHead
            newHead = nextNode
            nextNode = nextNode.next
        }
        
        newHead.next = prevNode
        return newHead
    }
    
    const merge1To1 = (list1, list2) => {
        const newHead = new ListNode()
        let temp = newHead
        let l1 = list1
        let l2 = list2
        
        while(l1 || l2){
            temp.next = l1
            l1 = l1.next
            temp = temp.next
            
            temp.next = l2
            l2 = l2 ? l2.next : null
            temp = temp.next
        }
        
        return list1
    }
    
    const [firstHalf, socondHalf] = splitToHalf(head)
    const reversedSecondHalf = reverseList(socondHalf)
    return merge1To1(firstHalf, reversedSecondHalf)
    
};