/**
 * @param {string} s
 * @return {number}
 */

class Node{
    constructor(val, next){
        this.val = val
        this.next = next
    }
}

const isDigit = (c) => {
    return c.charCodeAt(0) >= 48 && c.charCodeAt(0) < 58
}

var calculate = function(s) {
    const headNode = new Node()
    let temp = ""
    
    let tempHead = headNode
    for(let i = 0; i < s.length; i++){
        if(isDigit(s[i])){
            temp += s[i]
        }else if(['+', '-', '*', '/'].includes(s[i])){
            tempHead.next = new Node(parseInt(temp), new Node(s[i]))
            tempHead = tempHead.next.next
            temp = ""
        }
    }
    tempHead.next = new Node(parseInt(temp))
    
    tempHead = headNode.next
    while(tempHead && tempHead.next){
        const expNode = tempHead.next
        if(expNode.val === '*'){
            tempHead.val = tempHead.val * tempHead.next.next.val
            tempHead.next = tempHead.next.next.next
        }else if(expNode.val === '/'){
            tempHead.val = parseInt(tempHead.val / tempHead.next.next.val)
            tempHead.next = tempHead.next.next.next
        }else{
            tempHead = tempHead.next.next    
        }
        
    }
    
    tempHead = headNode.next
    while(tempHead && tempHead.next){
        const expNode = tempHead.next
        if(expNode.val === '+'){
            tempHead.val = tempHead.val + tempHead.next.next.val
            tempHead.next = tempHead.next.next.next
        }else if(expNode.val === '-'){
            tempHead.val = tempHead.val - tempHead.next.next.val
            tempHead.next = tempHead.next.next.next
        }
    }
    
    return headNode.next.val
};