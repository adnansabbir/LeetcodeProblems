/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b)=> a[0] - b[0])
    let result = [intervals[0]]
    
    for(let i = 1; i < intervals.length; i++){
        if(intervals[i][0] > result.at(-1)[1]){
            result.push(intervals[i])
            continue
        }
        
        if(intervals[i][1] <= result.at(-1)[1]) continue
        result.push([result.pop()[0], intervals[i][1]])
    }
    
    return result
};