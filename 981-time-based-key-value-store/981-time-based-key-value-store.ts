interface TimeValueMap{
    value: string 
    timestamp: number
}

class TimeMap {
    private data: Record<string, TimeValueMap[]>
        
    constructor() {
        this.data = {}
    }

    set(key: string, value: string, timestamp: number): void {
        if(this.data[key] === undefined){
            this.data[key] = []
        }
        
        const dataCollection = this.data[key]
        dataCollection.push({value, timestamp})
    }

    get(key: string, timestamp: number): string {
        if(this.data[key] === undefined) return ''
        const dataCollection = this.data[key]
        const indexOfData = this.searchClosestMinTime(dataCollection, timestamp)
        
        if(indexOfData === -1) return ''
        
        return dataCollection[indexOfData].value
    }

    searchClosestMinTime(collection: TimeValueMap[], time: number): number{
        if(!collection.length || time < collection[0].timestamp) return -1
        
        let start = 0, end = collection.length - 1
        while(start<=end){
            const mid = Math.floor((start+end)/2)
            
            if(collection[mid].timestamp === time) return mid
            else if(collection[mid].timestamp < time && (mid === end  || collection[mid+1].timestamp > time)) return mid
            else if(collection[mid].timestamp > time){
                end = mid - 1
            }else{
                start = mid + 1
            }
        }
        
        return -1
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */