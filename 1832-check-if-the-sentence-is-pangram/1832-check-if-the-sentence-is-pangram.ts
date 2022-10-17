function checkIfPangram(sentence: string): boolean {
    const charExists = new Array<boolean>(26).fill(false)
    
    const aValue = 'a'.charCodeAt(0)
    for(let i = 0; i<sentence.length; i++){
        const code = sentence[i].charCodeAt(0) - aValue
        charExists[code] = true
    }
    
    return charExists.every(c => c)
};