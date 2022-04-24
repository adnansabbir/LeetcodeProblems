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

// var UndergroundSystem = function() {
    
// };

// /** 
//  * @param {number} id 
//  * @param {string} stationName 
//  * @param {number} t
//  * @return {void}
//  */
// UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
    
// };

// /** 
//  * @param {number} id 
//  * @param {string} stationName 
//  * @param {number} t
//  * @return {void}
//  */
// UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    
// };

// /** 
//  * @param {string} startStation 
//  * @param {string} endStation
//  * @return {number}
//  */
// UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    
// };

/** 
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */