function makeEqual(words) {
    // Initialize frequency array for 26 lowercase English letters
    const freq = new Array(26).fill(0);

    // Count the frequency of each character in all words
    words.forEach(word => {
        for (let char of word) {
            freq[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }
    });
    
    // Check if each character's count is divisible by the number of words
    return freq.every(count => count % words.length === 0);
}