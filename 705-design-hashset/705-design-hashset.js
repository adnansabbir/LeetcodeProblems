class MyHashSet{
    constructor(key){
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