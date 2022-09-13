function validUtf8(data: number[]): boolean {
    const getNextBytesToCheck = (num: number):number => {
        if(num >= 0 && num<=127) return 0
        if(num >= 192 && num<=223) return 1
        if(num >= 224 && num<=239) return 2
        if(num >= 240 && num<=247) return 3
        return -1
    }
    
    const isValidNextByte = (num: number): boolean => {
        return num >= 128 && num <= 191    
    }
    
    let start = 0
    while(start < data.length){
        let nextNumsToCheck = getNextBytesToCheck(data[start++])
        if(nextNumsToCheck === -1) return false
        
        while(nextNumsToCheck){
            if(start >= data.length || !isValidNextByte(data[start])) return false
            start++
            nextNumsToCheck--
        }
    }
    
    return true
};