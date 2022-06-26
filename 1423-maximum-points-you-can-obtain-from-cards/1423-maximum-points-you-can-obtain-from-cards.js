/**
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */

var maxScore = function(cardPoints, k) {
    let minSum = 0
    let total = 0
    let size = cardPoints.length - k
    let sumOfSize = 0
    
    if(size === 0) return cardPoints.reduce((a, b) => a + b)
    
    for(let i = 0; i < size; i++){
        sumOfSize+= cardPoints[i]
    }
    total = sumOfSize
    minSum = sumOfSize
    
    for(let i = size; i < cardPoints.length; i++){
        total+=cardPoints[i]
        sumOfSize = sumOfSize - cardPoints[i-size] + cardPoints[i]
        minSum = Math.min(minSum, sumOfSize)
    }
    
    return total - minSum
};