function threeSumClosest(nums: number[], target: number): number {
    nums.sort((a,b) => a - b);
    
    let result = Infinity;
    let len = nums.length;
    
    for (let i = 0; i < len; i++) {
        if (i > 0 && nums[i]  === nums[i-1]) {
            continue;
        }
        const current = i;
        let left = i + 1;
        let right = len - 1;
        
        while (left < right) {
            let sum = nums[current];
            sum += nums[left];
            sum += nums[right];
            
            if (Math.abs(target - sum) < Math.abs(target - result)) {
                result = sum;
            }
            
            if (sum <= target) {
                left++;
            }
            
            if (sum >= target) {
                right--;
            }
        }
    }
    return result;
};