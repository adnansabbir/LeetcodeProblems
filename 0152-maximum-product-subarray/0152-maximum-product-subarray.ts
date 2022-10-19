function maxProduct(nums: number[]): number {
    
    const getProduct = (start: number, end: number): number =>{
        let product = nums[start]
        for(let i = start+1; i < end; i++) product*=nums[i]
        return product
    } 
    
    const getMaxProduct = (start: number, end: number, evenNegetives: boolean) => {
        if(start === end) return 0
        if(start === end-1) return nums[start]
        
        // if even negetives return product
        if(evenNegetives) return getProduct(start, end)
        
        // if odd negetives get the first and last negetive and split based on them
        let firstNegetive = null, lastNegetive = null
        for(let i = start; i<end; i++){
            if(nums[i] < 0){
                if(firstNegetive === null) firstNegetive = i
                lastNegetive = i
            }
        }
        
        return Math.max(getMaxProduct(firstNegetive+1, end, true), getMaxProduct(start, lastNegetive, true))
        
    }
    
    let maxProduct = nums[0]
    let lastZero = -1
    let negetiveCount = 0
    for(let i = 0; i<nums.length; i++){
        let product = 0
        if(nums[i] < 0) negetiveCount++
        
        if(nums[i] === 0){
            product = getMaxProduct(lastZero+1, i, negetiveCount%2 === 0)
            lastZero = i
            negetiveCount = 0
            maxProduct = Math.max(maxProduct, product)
        }else if(i === nums.length - 1){
            product = getMaxProduct(lastZero+1, i+1, negetiveCount%2 === 0)
            maxProduct = Math.max(maxProduct, product)
        }
    }
    
    if(lastZero === -1) return maxProduct
    if(maxProduct < 0) return 0
    return maxProduct
};