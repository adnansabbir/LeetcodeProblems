function longestPalindrome(s: string): number {
    const frequency = {}
    let size = 0
    for(let char of s){
        frequency[char] = (frequency[char] || 0) + 1
        if(frequency[char] === 2){
            size += frequency[char]
            frequency[char] = 0
        }
    }
    
    let extraSize = Object.keys(frequency).some(key=> !!frequency[key]) ? 1 : 0
    return size + extraSize
};