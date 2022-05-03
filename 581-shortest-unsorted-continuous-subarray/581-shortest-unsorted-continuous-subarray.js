/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function(nums) {
    let left = 0
    const n = nums.length - 1
    
    while(left < n && nums[left] <= nums[left+1]){
        left++
    }
    
    if(left === n) return 0
    
    const moveLeft = (idx, comp) => {
        if(idx === -1) return -1
        
        while( idx >= 0 && nums[idx] > comp){
            idx--
        }
        
        return idx
    }
    
    for(let i = left+1; i <= n; i++){
        left = moveLeft(left, nums[i])
        if(left === -1) break;
    }
    
    
    let right = n
    
    while(right > 0 && nums[right] >= nums[right - 1]){
        right--
    }
    
    const moveRight = (idx, comp) => {
        if(idx === n + 1) return n + 1
        
        while( idx <= n && nums[idx] < comp){
            idx++
        }
        
        return idx
    }
    
    for(let i = right - 1; i >= 0; i--){
        right = moveRight(right, nums[i])
        if(right === n + 1) break;
    }
    
    return (right - left) - 1
};