function findMin(nums: number[]): number {
    let start = 0, end = nums.length - 1
    
    if(nums[start] <= nums[end]) return nums[start]
    
    while(start < end){
        const mid = Math.floor((start+end)/2)
        if(nums[mid] > nums[mid+1]) return nums[mid+1]
        else if(nums[mid] < nums[mid-1]) return nums[mid]
        else if(nums[mid] > nums[0]){
            start = mid+1
        }else{
            end = mid-1
        }
    }
};