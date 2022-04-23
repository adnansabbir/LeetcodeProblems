class MyCircularDeque{
    constructor(k){
        this.size = k
        this.length = 0
        this.values = new Array(k)
        
        this.start = 0
        this.end = k - 1
    }
    
    _resetPosIfEmpty(){
        if(this.isEmpty()){
            this.start = 0
            this.end = this.size - 1
        }
    }
    
    _getPointerPosition(pos){
        if (pos === -1) return this.size - 1
        return pos % this.size
    }
    
    insertFront(value){
        if(this.isFull()) return false
        
        this.values[this.start] = value
        this.start = this._getPointerPosition(this.start + 1)
        this.length++
        return true
    }
    
    insertLast(value){
        if(this.isFull()) return false
        
        this.values[this.end] = value
        this.end = this._getPointerPosition(this.end - 1)
        this.length++
        return true
    }
    
    deleteFront(){
        if(this.isEmpty()) return false
        
        this.start = this._getPointerPosition(this.start - 1)
        this.values[this.start] = null
        this.length--
        
        this._resetPosIfEmpty()
        return true
    }
    
    deleteLast(){
        if(this.isEmpty()) return false
        
        this.end = this._getPointerPosition(this.end + 1)
        this.values[this.end] = null
        this.length--
        
        this._resetPosIfEmpty()
        return true
    }
    
    getFront(){
        if(this.isEmpty()) return -1
        
        return this.values[this._getPointerPosition(this.start - 1)]
    }
    
    getRear(){
        if(this.isEmpty()) return -1
        
        return this.values[this._getPointerPosition(this.end + 1)]
        
    }
    
    isEmpty(){
        return !this.length
    }
    
    isFull(){
        return this.length === this.size
    }
}
