class MyHashSet{
    constructor(key){
        this.size = Math.pow(10, 5) + 1;
        this.data = [];
    }
    
    _getHashKey(key){
        return key % this.size;
    }
    
    add(key){
        const hashKey = this._getHashKey(key)
        const bucket = this.data[hashKey]
        if(bucket === undefined){
            this.data[hashKey] = [key]
            return
        }
        
        if(bucket.indexOf(key) !== -1) return
        
        bucket.push(key)
    }
    
    remove(key){
        const hashKey = this._getHashKey(key)
        const bucket = this.data[hashKey]
        if(bucket === undefined || bucket.indexOf(key) === -1){
            return
        }
        
        bucket.pop(bucket.indexOf(key))
        if(!bucket.length){
            this.data[hashKey] = undefined
        }
    }
    
    contains(key){
        const hashKey = this._getHashKey(key)
        const bucket = this.data[hashKey]
        if(bucket === undefined){
            return false
        }
        
        return bucket.indexOf(key) !== -1
    }
}