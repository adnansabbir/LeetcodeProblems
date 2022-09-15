function findOriginalArray(changed: number[]): number[] {
    if(changed.length % 2 !== 0) return []
    const freq = {}
    changed.forEach(change=> {
        freq[change] = (freq[change] || 0) + 1
    })
    
    changed = changed.sort((a, b)=> a-b)
    const result = []
    for(let change of changed){
        if(freq[change] === 0) continue
        freq[change]--
        if(!freq[change*2]) return []
        freq[change*2]--
        result.push(change)
    }
    return result
};