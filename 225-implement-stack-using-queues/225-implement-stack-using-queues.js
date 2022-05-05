
var MyStack = function() {
    this.q1 = []
    this.q2 = []
    this.cQ = this.q2
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    if(this.cQ === this.q1){
        this.q2.push(x)
        while(this.cQ.length){
            this.q2.push(this.cQ.pop(0))
        }
        this.cQ = this.q2
    }else{
        this.q1.push(x)
        while(this.cQ.length){
            this.q1.push(this.cQ.shift())
        }
        this.cQ = this.q1
    }
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    
    return this.cQ.shift()
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    return this.cQ[0]
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return !this.cQ.length
};

var obj = new MyStack()

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */