function findMin(nums: number[]): number {
    const getSmallest = (start: number, end: number) => {
        if(start === end) return nums[start]
        // if there is one element retur that as min
        
        if(nums[start] < nums[end]) return nums[start]
        const mid = Math.floor((start+end)/2)
        return Math.min(getSmallest(start, mid), getSmallest(mid+1, end))
    }
    
    return getSmallest(0, nums.length-1)
};