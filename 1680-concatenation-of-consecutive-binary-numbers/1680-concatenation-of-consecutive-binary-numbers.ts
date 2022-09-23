function concatenatedBinary(n: number): number {
    let binaryResult = ""
    const MOD = BigInt(10**9 + 7)
    
    for(let i = 1; i <= n; i++){
        binaryResult += i.toString(2)
        if(binaryResult.length < 30) continue
        const temp = BigInt('0b' + binaryResult)
        binaryResult = (temp%MOD).toString(2)
    }
    
    return parseInt(binaryResult, 2)
};