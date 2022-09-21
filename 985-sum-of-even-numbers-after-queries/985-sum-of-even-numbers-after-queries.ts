function sumEvenAfterQueries(nums: number[], queries: number[][]): number[]{
	if(!nums || nums.length === 0 || !queries || queries.length === 0) return []
	
	let tempSum = 0
	
	// get initial sum of evens
	for(let num of nums){
		if(num%2 === 0){
			tempSum += num
		}
	}
	
	const result: number[] = []
	// pass through queries, update tempSum and add it to the result
	for(let [val, index] of queries){
		if(nums[index]%2 === 0){
			if((nums[index]+val)%2 === 0){
				tempSum += val
			}else{
				tempSum -= nums[index]
			}
		}else{
			if((nums[index]+val)%2 === 0){
				tempSum += nums[index]+val
			}
		}
		
		nums[index]+=val
		result.push(tempSum)
	}
	
	return result
}