class MyCircularDeque{
    constructor(k){
        this.size = k
        this.length = 0
        this.values = new Array(k)
        
        this.start = 0
        this.end = k - 1
    }
    
//     _setFirstValue(value){
//         this.start = 0
//         this.end = 0
//         this.values[0] = value
//         this.length++
//     }
    
//     _deleteLastValue(){
//         this.values[this.start] = null
//         this.length--
//         this.start = null
//         this.end = null
//     }
    
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
// /**
//  * @param {number} k
//  */
// var MyCircularDeque = function(k) {
    
// };

// /** 
//  * @param {number} value
//  * @return {boolean}
//  */
// MyCircularDeque.prototype.insertFront = function(value) {
    
// };

// /** 
//  * @param {number} value
//  * @return {boolean}
//  */
// MyCircularDeque.prototype.insertLast = function(value) {
    
// };

// /**
//  * @return {boolean}
//  */
// MyCircularDeque.prototype.deleteFront = function() {
    
// };

// /**
//  * @return {boolean}
//  */
// MyCircularDeque.prototype.deleteLast = function() {
    
// };

// /**
//  * @return {number}
//  */
// MyCircularDeque.prototype.getFront = function() {
    
// };

// /**
//  * @return {number}
//  */
// MyCircularDeque.prototype.getRear = function() {
    
// };

// /**
//  * @return {boolean}
//  */
// MyCircularDeque.prototype.isEmpty = function() {
    
// };

// /**
//  * @return {boolean}
//  */
// MyCircularDeque.prototype.isFull = function() {
    
// };

// /** 
//  * Your MyCircularDeque object will be instantiated and called as such:
//  * var obj = new MyCircularDeque(k)
//  * var param_1 = obj.insertFront(value)
//  * var param_2 = obj.insertLast(value)
//  * var param_3 = obj.deleteFront()
//  * var param_4 = obj.deleteLast()
//  * var param_5 = obj.getFront()
//  * var param_6 = obj.getRear()
//  * var param_7 = obj.isEmpty()
//  * var param_8 = obj.isFull()
//  */