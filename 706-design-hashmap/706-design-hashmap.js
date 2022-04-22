class MyHashMap{
    put(key, value){
        this[key] = value
        
    }
    
    get(key){
        if(this[key] === undefined) return -1
        
        return this[key]
    }
    
    remove(key){
        if(!this[key]) return
        delete this[key]
    }
}