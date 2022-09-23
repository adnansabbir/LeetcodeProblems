function concatenatedBinary(n: number): number {
    let result = BigInt(1)
    const MOD = BigInt(10**9 + 7)
    
    for(let i = 2; i <= n; i++){
        const lengthOfIinBinary = BigInt(Math.floor(Math.log(i)/Math.log(2))+1)
        result = ((result<<lengthOfIinBinary) | BigInt(i)) % MOD
    }
    
    return Number(result)
};