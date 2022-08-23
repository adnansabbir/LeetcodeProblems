function countBits(n: number): number[] {
    const findNumberOfBits = (n)=> {
        let count = 0
        while(n>0){
            count += n&1
            n = n>>1
        }
        return count
    }
    
    const result:number[] = []
    for(let i = 0; i<= n; i++){
        result.push(findNumberOfBits(i))
    }
    
    return result
};