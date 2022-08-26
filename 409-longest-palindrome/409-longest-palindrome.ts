function longestPalindrome(s: string): number {
    const frequency = {}
    let size = 0
    const oddChars = new Set<string>()
    for(let char of s){
        frequency[char] = (frequency[char] || 0) + 1
        oddChars.add(char)
        if(frequency[char] === 2){
            size += frequency[char]
            frequency[char] = 0
            oddChars.delete(char)
        }
    }
    
    let extraSize = oddChars.size ? 1 : 0
    return size + extraSize
};