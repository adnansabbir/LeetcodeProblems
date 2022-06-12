/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function(nums) {
   let left = 0
   let right = 0
   let elem = new Set()
   let max_sum = 0
   let total = 0
   
   while(right < nums.length){
       while(elem.has(nums[right])){
           elem.delete(nums[left])
           total -= nums[left++]
       }
       
       elem.add(nums[right])
       total += nums[right++]
       
       
       if(total > max_sum){
           max_sum = total
       }
       // console.log(total, left, right, elem)
   }
    
    return max_sum
};