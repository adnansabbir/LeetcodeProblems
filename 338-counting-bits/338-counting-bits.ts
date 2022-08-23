function countBits(n: number): number[] {
    if(n == 0) return [0]
    if(n == 1) return [0,1]
    const result:number[] = new Array<number>(n+1)
    result[0] = 0
    result[1] = 1
    
    let pointer = 0
    let pos = 2
    while(pos <= n){
        if(Math.log(pos)/Math.log(2)%1 == 0){
            result[pos] = 1
            pointer = 0
        }else{
            result[pos] = 1 + result[++pointer]
        }
        pos+=1
    }
    
    return result
};