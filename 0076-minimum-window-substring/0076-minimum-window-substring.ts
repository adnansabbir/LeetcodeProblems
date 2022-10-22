// A - 0
// B - 0
// C - 0
// total = 0

// ADOBECOEDBANC
// left and right starts at 0
// move right till we get all the letters at S
// move right by each character, if we get a char at t try to reduce left pointer

function minWindow(s: string, t: string): string {
    const tFreq = {}
    let charLeftToBalance = t.length
    for(let i = 0; i<t.length; i++){
        tFreq[t[i]] = (tFreq[t[i]] || 0) + 1
    }
        
    let minSubString = ''
    let left = 0, right = 0
    
    while(right < s.length){
        if(s[right] in tFreq){
            tFreq[s[right]]--
            if(tFreq[s[right]] >= 0){
                charLeftToBalance--
            }
            
            while(!(s[left] in tFreq) || (tFreq[s[left]] !== undefined && tFreq[s[left]] < 0)){
                if((tFreq[s[left]] !== undefined && tFreq[s[left]] < 0)){
                    tFreq[s[left]]++
                }
                left++
            }
            
            if(charLeftToBalance === 0 && (!minSubString || right - left < minSubString.length)){
                minSubString = s.substring(left, right+1)
            }
        }
        
        right++
    }
    
    return minSubString
};