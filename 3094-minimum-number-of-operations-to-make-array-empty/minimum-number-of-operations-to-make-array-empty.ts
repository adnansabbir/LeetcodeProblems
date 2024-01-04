function minOperations(nums: number[]): number {
        const freq: Map<number, number> = new Map();  // Map to store frequencies

        // Count frequencies
        nums.forEach(num => {
            freq.set(num, (freq.get(num) || 0) + 1);
        });

        let result = 0;
        // Iterate through the frequencies
        for(const num of freq.keys()){
            // If any number appears once, it's impossible to perform the operation
            if (freq.get(num) < 2) {
                return -1;
            }
            // Calculate the operations needed using ceiling to account for incomplete pairs/triplets
            result += Math.ceil(freq.get(num) / 3);
        };

        return result;  // Return the total number of operations
    }