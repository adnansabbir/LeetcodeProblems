function breakPalindrome(palindrome: string): string {
    if(palindrome.length === 1) return ''
    
    const halfSize = Math.floor(palindrome.length/2)
    
    for(let i = 0; i < halfSize; i++){
        if(palindrome[i] !== 'a') return `${palindrome.substring(0,i)}a${palindrome.substring(i+1)}`
    }
    
    return `${palindrome.substring(0,palindrome.length-1)}b`
};