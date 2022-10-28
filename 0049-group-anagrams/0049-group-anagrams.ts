function groupAnagrams(strs: string[]): string[][] {
    
    const getHash = (str: string) => {
        const frequency = new Array<number>(26).fill(0)
        const baseCharCode = 'a'.charCodeAt(0)
        for(let i = 0; i<str.length; i++){
            frequency[str[i].charCodeAt(0) - baseCharCode]++
        }
        let hash = ''
        for(let i = 0; i<frequency.length; i++){
            if(frequency[i]){
                const char = String.fromCharCode(i+baseCharCode)
                hash += frequency[i] === 1 ? char: `${char}${frequency[i].toString()}`
            }
        }
        return hash
    }
    
    const groups: Record<string, string[]> = {}
    for(let i = 0; i< strs.length; i++){
        const hash = getHash(strs[i])
        if(!(hash in groups)) groups[hash] = []
        groups[hash].push(strs[i])
    }
    
    const result = []
    Object.values(groups).forEach(group => result.push(group))
    return result
};