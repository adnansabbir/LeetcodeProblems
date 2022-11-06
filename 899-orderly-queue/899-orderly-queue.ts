function orderlyQueue(s: string, k: number): string {
    if(k===1){
        let minS = s
        let nextS = s
        for(let i = 0; i<s.length; i++){
            nextS = nextS.substring(1) + nextS[0]
            console.log(nextS, minS)
            if(nextS < minS) minS = nextS
        }

        return minS
    }

    return s.split('').sort().join('')
}