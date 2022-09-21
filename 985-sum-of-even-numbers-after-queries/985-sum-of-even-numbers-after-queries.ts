function sumEvenAfterQueries(nums: number[], queries: number[][]): number[]{
	if(!nums || nums.length === 0 || !queries || queries.length === 0) return []
	
	// get initial sum of evens
	let tempSum = nums.filter(num => num%2 === 0).reduce((a, b) => a + b, 0)
	
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