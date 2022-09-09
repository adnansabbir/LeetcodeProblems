function numberOfWeakCharacters(properties: number[][]): number {    
    properties = properties.sort((a,b)=> a[0]===b[0] ? a[1]-b[1] : a[0]-b[0])
    const size = properties.length - 1
    
    const attacks = {}
    for(let i = 0; i<=size; i++){
        let prop = properties[i]
        if(!attacks[prop[0]]){
            attacks[prop[0]] = [i, -1]
            if(i!=0){
                attacks[properties[i-1][0]][1] = i
            }
        }
    }
    // console.log(properties)
    // console.log(attacks)
    
    const largestFromLast = new Array<number>(properties.length)
    for(let i = size; i>=0; i--){
        if(i==size){
            largestFromLast[i] = properties[i][1]
        }else{
            largestFromLast[i] = Math.max(largestFromLast[i+1], properties[i][1])
        }
    }
    
    const hasLargerDefence=(start:number, value: number):boolean=>{
        let end = size
        while(start<=end){
            const mid = Math.floor((start+end)/2)
            if(largestFromLast[mid]>value) return true
            else if(largestFromLast[mid]<=value){
                end=mid-1
            }else{
                start=mid+1
            }
        }
        return false
    }

    let weakCaharacters = 0
    for (let prop of properties){
        const largerAttackIndex = attacks[prop[0]][1]
        if(largerAttackIndex===-1) continue
        if(hasLargerDefence(largerAttackIndex, prop[1])){
            weakCaharacters++
        }
    }
    
    return weakCaharacters
};