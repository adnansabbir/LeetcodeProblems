function maxLengthBetweenEqualCharacters(s) {
        // Initialize an array to keep track of the first occurrence index for each character
        const initialCharIndex = new Array(26).fill(-1);

        // Initialize the maximum substring length as -1, assuming no repeats initially
        let maxSubString = -1;

        // Iterate over each character in the string
        [...s].forEach((char, i) => {
            // Convert character to index (0 for 'a', 1 for 'b', etc.)
            const charIndex = char.charCodeAt(0) - 'a'.charCodeAt(0);
            if (initialCharIndex[charIndex] === -1) {
                // If it's the first occurrence, record the index
                initialCharIndex[charIndex] = i;
            } else {
                // If it's a repeat occurrence, calculate the gap and possibly update maxSubString
                maxSubString = Math.max(maxSubString, i - initialCharIndex[charIndex] - 1);
            }
        });
        
        // Return the maximum substring length found
        return maxSubString;
    }