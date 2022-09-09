function numberOfWeakCharacters(properties: number[][]): number {    
    properties = properties.sort((a,b)=> a[0]===b[0] ? a[1]-b[1] : a[0]-b[0])
    const size = properties.length - 1
    const getIndexOfNextLargerAttack=(value: number):number=>{
        let start = 0
        let end = size
        
        while(start<=end){
            const mid = Math.floor((start+end)/2)
            if(properties[mid][0]>value && properties[mid-1][0]==value) return mid
            else if(properties[mid][0]<=value){
                start=mid+1
            }else{
                end=mid-1
            }
        }
        return -1
    }
    
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
        const largerAttackIndex = getIndexOfNextLargerAttack(prop[0])
        if(largerAttackIndex===-1) continue
        if(hasLargerDefence(largerAttackIndex, prop[1])){
            weakCaharacters++
        }
        // console.log(prop, largerAttackIndex, hasLargerDefence(largerAttackIndex, prop[1]))
    }
    
    return weakCaharacters
};