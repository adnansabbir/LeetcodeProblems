class UndergroundSystem{
    constructor(){
        this.src_dest_map = {}
        this.records = {}
    }
    
    checkIn(id, stationName, t){
        this.records[id] = {id, stationName, t}
    }
    
    checkOut(id, stationName, t){
        const source = this.records[id]
        const key = `${source.stationName}-${stationName}`
        
        if(this.src_dest_map[key] === undefined){
            this.src_dest_map[key] = {avg: 0, size: 0}
        }
        
        let  {avg, size} = this.src_dest_map[key]
        size += 1
        avg -= avg / size
        avg += (t - source.t) / size
        this.src_dest_map[key] = {avg, size}
    }
    
    getAverageTime(startStation, endStation){
        const key = `${startStation}-${endStation}`
        return this.src_dest_map[key].avg
    }
}