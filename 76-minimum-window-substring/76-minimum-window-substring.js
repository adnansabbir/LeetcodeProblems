/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */

var minWindow = function(s, t) {
    if(t.length === 1) return s.includes(t) ? t : ""
    const tCount = new Proxy({}, {get: (target, props) => props in target ? target[props] : 0})
    for(let ch of t){
        tCount[ch]++
    }
    
    const required = Object.keys(tCount).length
    
    const filteredS = []
    for(let i = 0; i < s.length; i++){
       if(s[i] in tCount){
          filteredS.push([s[i], i])
        } 
    }
    
    let l = 0
    let r = 0
    let formed = 0
    const window = new Proxy({}, {get: (target, props) => props in target ? target[props] : 0})
    let result = [Infinity, null, null]
    
    while (r < filteredS.length){
        const rch = filteredS[r][0]
        window[rch] = window[rch] + 1
        
        if(window[rch] === tCount[rch]){
            formed++
        }
        
        while(l <= r && formed === required){
            const lch = filteredS[l][0]
            const start = filteredS[l][1]
            const end = filteredS[r][1]
            
            if(end - start + 1 < result[0]){
                result = [end - start + 1, start, end]
            }
            
            window[lch]--
            if(window[lch] < tCount[lch]){
                formed--
            }
            
            l++
        }
        
        r++
    }
   
    return result[0] === Infinity ? "" : s.substring(result[1], result[2] + 1)
};