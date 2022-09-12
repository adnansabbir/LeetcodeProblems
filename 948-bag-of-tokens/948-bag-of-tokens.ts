function bagOfTokensScore(tokens: number[], power: number): number {
    tokens = tokens.sort((a,b)=> a-b)
    let score = 0
    let start = 0, end = tokens.length-1
    let maxScore = 0

    while(start <= end){
        if(tokens[start] <= power){
            score++
            power-=tokens[start++]
        }else if(score && start < end){
            score--
            power+=tokens[end--]
        }else{
            break
        }
        console.log({start,end,power,score})
    }
    
    return score
};