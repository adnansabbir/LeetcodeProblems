function longestSubstring(s: string, k: number): number {
    if(k > s.length) return 0
    
    const getFirstFrequencyBelowK = (start: number, end: number): null | {char: string, index: number} => {
        const frequency = new Array<number>(26).fill(0)
        const base = 'a'.charCodeAt(0)
        for(let i = start; i < end; i++){
            frequency[s[i].charCodeAt(0) - base]++
        }
        for(let i = start; i < end; i++){
            if(frequency[s[i].charCodeAt(0) - base] < k) return {char: s[i], index: i}
        }
        
        return null
    }
    
    const getMaxSubstring = (start: number, end: number): number => {
        if(end - start < k) return 0
        const splitAtChar = getFirstFrequencyBelowK(start, end)
        if(splitAtChar === null) return end - start
        const left = getMaxSubstring(start, splitAtChar.index)
        const right = getMaxSubstring(splitAtChar.index + 1, end)
        
        return Math.max(left, right)
    }
    
    return getMaxSubstring(0, s.length)
    // abcdddabc - 3
    
};