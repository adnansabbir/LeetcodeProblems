/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */

const lcs = (w1, w2) => {
    const matrix = new Array(w1.length + 1).fill(0).map(_ => new Array(w2.length + 1).fill(0))
    for(let i = 1; i <= w1.length; i++){
        for(let j = 1; j <= w2.length; j++){
            if(w1[i-1] === w2[j-1]){
                matrix[i][j] = 1 + matrix[i-1][j-1]
            }else{
                matrix[i][j] = Math.max(matrix[i-1][j], matrix[i][j-1])
            }
        }
    }
    return matrix.at(-1).at(-1)
}

var minDistance = function(word1, word2) {
    return (word1.length + word2.length) - (2 * lcs(word1, word2))
    
};