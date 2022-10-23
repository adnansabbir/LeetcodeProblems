function findErrorNums(nums: number[]): number[] {
    const checkedNums = new Set<number>()
    let duplicate: number = null, total = 0
    
    for(let num of nums){
        if(checkedNums.has(num)){
            duplicate = num
        }else{
            total += num
            checkedNums.add(num)
        }
    }

    const size = nums.length
    const sumOfN = (size*(size+1))/2
    
    return [duplicate, sumOfN - total]
};