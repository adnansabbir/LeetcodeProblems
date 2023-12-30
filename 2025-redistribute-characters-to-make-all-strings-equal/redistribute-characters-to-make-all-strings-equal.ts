function makeEqual(words: string[]): boolean {
    // Initialize frequency array for 26 lowercase English letters
    const freq = new Array(26).fill(0);

    // Count the frequency of each character in all words
    for (let word of words) {
        for (let char of word) {
            freq[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }
    }
    
    // Check if each character's count is divisible by the number of words
    for (let count of freq) {
        if (count % words.length !== 0) {
            return false;
        }
    }
    
    return true;
}
