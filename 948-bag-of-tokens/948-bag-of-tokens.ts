function bagOfTokensScore(tokens: number[], power: number): number {
    tokens = tokens.sort((a,b)=> a-b)
    let score = 0
    let start = 0, end = tokens.length-1
    let maxScore = 0

    while(start <= end){
        if(tokens[start] > power){
            if(score<1) break
            score--
            power+=tokens[end--]
        }else{
            score++
            maxScore = Math.max(maxScore, score)
            power-=tokens[start++]
        }
    }
    
    return maxScore
};