function search(nums: number[], target: number): number {
    let start = 0, end = nums.length - 1
    
    // [4,5,6,0,1,2,3] -2
    while(start <= end){
        const mid = Math.floor((start+end)/2)
        
        if(nums[mid] === target) return mid
        else if(nums[start] <= nums[mid]){
            // left is sorted and work in this
            if(target >= nums[start] && target < nums[mid]) end = mid-1
            else start = mid + 1
        }else{
            // right side is sorted
            if(target > nums[mid] && target <= nums[end]) start = mid+1
            else end = mid - 1
        }
    }
    
    return -1
};