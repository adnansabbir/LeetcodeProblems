function findMatrix(nums: number[]): number[][] {
        const frequencies: { [key: number]: number } = {};  // Store frequencies of elements

        let maxFrequency = 0;  // Track the maximum frequency
        nums.forEach(num => {  // Count the frequency of each number
            frequencies[num] = (frequencies[num] || 0) + 1;
            maxFrequency = Math.max(maxFrequency, frequencies[num]);  // Update max frequency
        });

        const result: number[][] = Array.from({ length: maxFrequency }, () => []);  // Create a 2D array with rows equal to max frequency

        Object.keys(frequencies).forEach(key => {  // Distribute each number into the 2D array
            const num = parseInt(key);
            for (let j = 0; j < frequencies[num]; j++) {  // For each occurrence of the number
                result[j].push(num);  // Append the number to the corresponding row
            }
        });

        return result;
    }