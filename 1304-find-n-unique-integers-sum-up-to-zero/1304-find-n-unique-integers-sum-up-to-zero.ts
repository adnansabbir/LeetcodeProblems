function sumZero(n: number): number[] {
    const result = []
    
    for(let i = 1; i<=n/2; i++){
        result.push(i)
        result.push(-i)
    }
    
    if(result.length < n) result.push(0)
    return result
};