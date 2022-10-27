function largestOverlap(img1: number[][], img2: number[][]): number {
    const N = img1.length
        const getOverlapCountWithShift = ([x, y]: number[], img: number[][], ref: number[][]): number => {
            let rightShift = 0
            let leftShift = 0
            
            // y++ -> Shifting right
            // x++ -> Shift Down
            let rRow = 0
            for(let mRow = x; mRow < N; mRow++){
                let rCol = 0
                for(let mCol = y; mCol < N; mCol++){
                    if(img[mRow][mCol] + ref[rRow][rCol] >= 2) rightShift++
                    if(img[mRow][rCol] + ref[rRow][mCol] >= 2) leftShift++
                    rCol++
                }
                rRow++
            }
            
            return Math.max(rightShift, leftShift)
        }


        let maxOverLap = 0
        for(let i = 0; i < N; i++){
            for(let j = 0; j < N; j++){
                maxOverLap = Math.max(maxOverLap, getOverlapCountWithShift([i,j], img1, img2))
                maxOverLap = Math.max(maxOverLap, getOverlapCountWithShift([i,j], img2, img1))
            }
        }
        
    
    // [0,1]   [0,0]
    // [0,0]   [1,0]
        return maxOverLap
};