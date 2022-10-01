function numDecodings(s: string): number {
    if(s[0]==='0') return 0
    
    const dp = new Array<number>(s.length).fill(0)
    let parentCombination = 1
    let grandCombination = 1
    
    for(let i = 1; i < s.length; i++){
        const currentChar = s[i]
        const prevChar = s[i-1]
        
        let currentCombination = currentChar !== '0' ? parentCombination : 0
        
        const biggerCharAscii = parseInt(prevChar + currentChar)
        const canFormLargerChar = biggerCharAscii>=10 && biggerCharAscii<=26
        if(canFormLargerChar){
            currentCombination += grandCombination
        }

        if(currentCombination === 0){
            return 0
        }
        
        grandCombination = parentCombination
        parentCombination = currentCombination
    }
    
    return parentCombination
};