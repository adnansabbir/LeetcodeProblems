/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @constructor
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {
    this.data = nestedList
    this.pointer = 0
};


/**
 * @this NestedIterator
 * @returns {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    if(this.pointer >= this.data.length) return false
    
    let data = this.data[this.pointer]
    // console.log('hasnext ', data)
    
    if(data instanceof NestedIterator){
        const dataHasNext = data.hasNext()
        if(dataHasNext) return true
        
        this.pointer++
        return this.hasNext()
    }
    
    if(!data.isInteger()){
        this.data[this.pointer] = new NestedIterator(data.getList())
        return this.hasNext()
    }
    
    return true
};

/**
 * @this NestedIterator
 * @returns {integer}
 */
NestedIterator.prototype.next = function() {
    const data = this.data[this.pointer]
    
    if(data instanceof NestedIterator){
        return data.next()
    }
    // console.log('next ', data)
    this.pointer++
    return data.getInteger()
};

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/