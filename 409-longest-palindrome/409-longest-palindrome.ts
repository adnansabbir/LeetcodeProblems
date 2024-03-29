function longestPalindrome(s: string): number {
    const frequency = {}
    let size = 0
    let oddSize = 0
    for(let char of s){
        frequency[char] = (frequency[char] || 0) + 1
        oddSize+=1
        if(frequency[char] === 2){
            size += frequency[char]
            frequency[char] = 0
            oddSize-=2
        }
    }
    
    let extraSize = oddSize ? 1 : 0
    return size + extraSize
};