function sumEvenAfterQueries(nums: number[], queries: number[][]): number[]{
	if(!nums || nums.length === 0 || !queries || queries.length === 0) return []
	
	// get initial sum of evens
	let tempSum = nums.filter(num => num%2 === 0).reduce((a, b) => a + b, 0)
	
	const result: number[] = []
	
	return queries.map(([val, index])=> {
		const isEven = nums[index]%2 === 0
		const willBeEven = (nums[index]+val)%2 === 0
		tempSum += isEven ? willBeEven ? val : nums[index]*-1 : !willBeEven ? 0 : nums[index]+val
		nums[index]+=val
		return tempSum
	})
}