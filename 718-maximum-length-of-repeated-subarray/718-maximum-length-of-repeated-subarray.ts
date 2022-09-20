function findLength(nums1: number[], nums2: number[]): number {
    const dp = new Array<number[]>(2).fill([]).map(_ => new Array<number>(nums2.length).fill(0))
    // const dp = new Array<number[]>(nums1.length).fill(null).map(_ => new Array<number>(nums2.length).fill(0))
    let result = 0
    for(let i = 0; i<nums1.length; i++){
        for(let j = 0; j<nums2.length; j++){
            if(nums1[i] === nums2[j]){
                dp[i%2][j] = 1 + (j > 0 ? dp[(i+1)%2][j-1] : 0)
                result = Math.max(result, dp[i%2][j])
            }else{
                dp[i%2][j] = 0
            }
        }
    }
    return result
};