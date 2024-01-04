function minOperations(nums) {
        const freq = {};  // Object to store frequencies

        // Count frequencies
        nums.forEach(num => {
            freq[num] = (freq[num] || 0) + 1;
        });

        let result = 0;
        // Iterate through the properties in freq
        for (const num in freq) {
            // If any number appears once, it's impossible to perform the operation
            if (freq[num] < 2) {
                return -1;
            }
            // Calculate the operations needed using ceiling to account for incomplete pairs/triplets
            result += Math.ceil(freq[num] / 3);
        }

        return result;  // Return the total number of operations
    }
