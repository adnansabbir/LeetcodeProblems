class DLL{
    constructor(val = null, key = null, prev = null, next = null){
        this.val = val
        this.prev = prev
        this.next = next
        this.key = key
    }
}

class LRUCache{
    constructor(capacity){
        this.capacity = capacity
        this.size = 0
        
        this.head = new DLL()
        this.tail = new DLL(null, null, this.head)
        this.head.next = this.tail
        
        this.ref = {}
    }
    
    get(key){
        if(this.ref[key] === undefined) return -1
        
        const node = this._removeNode(this.ref[key])
        this._addNodeToEnd(node)
        
        return node.val
    }
    
    put(key, value){
        if(this.ref[key] === undefined){
            // add new node to the end
            // add new ref
            const newNode = new DLL(value, key)
            this._addNodeToEnd(newNode)
            this.ref[key] = newNode
            this.size++
            
            // check size
            // if size is full -> remove first node and it's ref
            if(this.size > this.capacity){
                this.size--
                const removedNode = this._removeNode(this.head.next)
                this.ref[removedNode.key] = undefined
            }
            
            return
        }
        
        // if key is already at the end, update value and return
        if(this.tail.prev.key === key){
            this.tail.prev.val = value
            return
        }else{
            // move the node to end and update value
            const node = this._removeNode(this.ref[key])
            node.val = value
            this._addNodeToEnd(node)
            return
        }
        
    }
    
    _removeNode(node){
        if(!node) return
        const prevNode = node.prev
        const nextNode = node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        return node
    }
    
    _addNodeToEnd(node){
        const lastNode = this.tail.prev
        lastNode.next = node
        node.next = this.tail
        node.prev = lastNode
        this.tail.prev = node
    }
}