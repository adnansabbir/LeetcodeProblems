function findAnagrams(s: string, p: string): number[] {
    if(p.length > s.length || !p.length) return []
    
    const baseCharCode = 'a'.charCodeAt(0)
    const pFrequency = new Array<number>(26).fill(0)
    for(let i = 0; i<p.length; i++){
        pFrequency[p[i].charCodeAt(0) - baseCharCode]++
    }
    
    const frequencyMatched = (f1: number[], f2: number[]) => {
        for(let i = 0; i<f1.length; i++){
            if(f1[i] !== f2[i]) return false
        }
        return true
    }
    
    const result = []
    const sFrequency = new Array<number>(26).fill(0)
    let left = 0, right = 0
    while(right < p.length){
        sFrequency[s[right++].charCodeAt(0) - baseCharCode]++
    }
    
    if(frequencyMatched(pFrequency, sFrequency)) result.push(left)
    while(right < s.length){
        sFrequency[s[right++].charCodeAt(0) - baseCharCode]++
        sFrequency[s[left++].charCodeAt(0) - baseCharCode]--
        if(frequencyMatched(pFrequency, sFrequency)) result.push(left)
    }
    
    return result
};