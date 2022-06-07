/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

let insertIntoPosition = (arr, idx, val)=> {
    for(let i = arr.length-1; i>idx; i--){
        arr[i] = arr[i-1]
    }
    arr[idx] = val;
};

var merge = function(nums1, m, nums2, n) {
    const result = [];
    let p1 = 0;
    let p2 = 0;
    let mInit = m;
    
    while (p1 < m && p2 < n){
        if(nums2[p2] > nums1[p1]){
            p1++;
        }else{
            insertIntoPosition(nums1, p1, nums2[p2]);
            p2++;
            m++;
        }
    }
    for(let i = mInit+p2; i<nums1.length; i++){
        nums1[i] = nums2[p2++];
    }
    // console.log(nums1, p2);
};