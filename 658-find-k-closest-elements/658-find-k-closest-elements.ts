function findClosestElements(arr: number[], k: number, x: number): number[] {
    let numbersStart = 0
    let closestNumbersStart = 0
    
    while(numbersStart < arr.length - k){
        const differenceWithFirst = Math.abs(arr[numbersStart] - x)
        const differenceWithLast = Math.abs(arr[numbersStart + k] - x)
        numbersStart++
        if(differenceWithLast < differenceWithFirst){
            closestNumbersStart = numbersStart
        }else if(differenceWithLast > differenceWithFirst){
            break
        }
    }
    
    return arr.slice(closestNumbersStart, closestNumbersStart+k)
};