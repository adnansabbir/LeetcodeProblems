function makeGood(s: string): string {
    const caseDifference = 'a'.charCodeAt(0) - 'A'.charCodeAt(0)
    let pointer = 0
    while(pointer < s.length - 1){
        const charCode = s[pointer].charCodeAt(0)
        const nextCharCode = s[pointer+1].charCodeAt(0)
        console.log(charCode, nextCharCode, caseDifference)
        if(
            (charCode + caseDifference === nextCharCode) ||
            (charCode - caseDifference === nextCharCode)
        ){
            s = s.substring(0, pointer) + s.substring(pointer+2)
            pointer = Math.max(0, pointer-1)
        }else pointer++
    }
    return s
};