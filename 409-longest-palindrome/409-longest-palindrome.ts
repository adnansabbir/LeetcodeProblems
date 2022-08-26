function longestPalindrome(s: string): number {
    const frequency = {}
    for(let char of s){
        frequency[char] = (frequency[char] || 0) + 1
    }
    
    let size = 0
    let extraSize = 0
    Object.keys(frequency).forEach(key=> {
        if(frequency[key] %2 == 0){
            size+=frequency[key]
        }else if(frequency[key] %2 == 1){
            size+=frequency[key]-1
            extraSize = 1
        }
    })
    return size + extraSize
};