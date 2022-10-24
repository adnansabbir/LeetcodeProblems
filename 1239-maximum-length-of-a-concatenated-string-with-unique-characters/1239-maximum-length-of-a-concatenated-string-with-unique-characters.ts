function maxLength(arr: string[]): number {
    let maxLength = 0
    
    const hasUniqueCharacters = (str: string): boolean => {
        const avoid = new Set<string>()
        for(let i = 0; i<str.length; i++){
            if(avoid.has(str[i])) return false
            else avoid.add(str[i])
        }
        return true
    }
    
    const traverse = (currString: string, idx: number): number => {
        if(idx > arr.length) return hasUniqueCharacters(currString) ? currString.length : 0
        if(!hasUniqueCharacters(currString)) return 0
        
        const lengthWithCurr = traverse(currString + arr[idx], idx+1)
        if(lengthWithCurr === 26) return 26
        const lengthWithoutCurr = traverse(currString, idx+1)
        
        return Math.max(lengthWithCurr, lengthWithoutCurr)
    }
    
    return traverse('', 0)
};