function pushDominoes(dominoes: string): string {
    let curr = 1
    let last = 0
    const domArr = dominoes.split('')
    
    const fill = (start: number, end: number, char: string) => {
        for(let i = start; i < end; i++){
            domArr[i] = char
        }
    }
    
    while(curr < domArr.length){
        if(domArr[curr] === '.'){
            curr++
            continue
        }
        
        const lastDotAndCurrentL = domArr[last] === '.' && domArr[curr] === 'L'
        const currentAndLastIsSame = domArr[last] === domArr[curr]
        
        if(lastDotAndCurrentL || currentAndLastIsSame){
            fill(last, curr, domArr[curr])
        }else if(domArr[last] === 'R' && domArr[curr] === 'L'){
            const skipMiddle = (last + curr) % 2 === 0
            const center = Math.ceil((last + curr) / 2)
            
            fill(last, center, 'R')
            if(skipMiddle){
                fill(center+1, curr, 'L')
            }else{
                fill(center, curr, 'L')
            }
        }
        
        last = curr
        curr++
    }
    if(curr === domArr.length && domArr[last] === 'R') fill(last, curr, 'R')
    
    return domArr.join('')
};