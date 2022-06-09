/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */

const search = (arr, start, target) => {
    let end = arr.length - 1
    while(start <= end){
        const mid = parseInt((start + end)/2)
        if(arr[mid] === target) return mid
        if(arr[mid] > target){
            end = mid - 1
        }else{
            start = mid + 1
        }
    }
    
    return -1
}

var twoSum = function(numbers, target) {
    for(let i = 0; i < numbers.length; i++){
        const numberToFind = target - numbers[i]
        const idx2 = search(numbers, i + 1, numberToFind)
        if(idx2 !== -1) return [i+1, idx2+1]
    }
    
    return []
};