class MyHashSet{
    constructor(key){
    }
    
    _getHashKey(key){
        return key % this.size;
    }
    
    add(key){
        this[key] = true
    }
    
    remove(key){
        this[key] = false
    }
    
    contains(key){
        return !!this[key]
    }
}