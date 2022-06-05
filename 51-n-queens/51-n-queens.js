/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const result = []
    const queens = new Array(n).fill(0).map(_ => new Array(n).fill('.'))
    
    const appendQueenToResult = () => {
        const queenCopy = []
        queens.forEach((r, i) => {
            queenCopy.push(r.join(''))
        })
        result.push(queenCopy)
    }
    
    const placeQueens = (row, bookedCols, bookedPosD, bookedNegD) => {
        
        for(let i = 0; i < n; i++){
            const col = i
            const posD = row + i
            const negD = row - i
            
            if(bookedCols.has(col) || bookedPosD.has(posD) || bookedNegD.has(negD)) continue
            
            queens[row][i] = "Q"
            
            if(row === n - 1){
                appendQueenToResult()
                queens[row][i] = "."
                continue
            }
            
            bookedCols.add(col)
            bookedPosD.add(posD)
            bookedNegD.add(negD)
            
            placeQueens(row + 1, bookedCols, bookedPosD, bookedNegD)
            
            bookedCols.delete(col)
            bookedPosD.delete(posD)
            bookedNegD.delete(negD)
            queens[row][i] = "."
        }
    }
    
    placeQueens(0, new Set(), new Set(), new Set())
    
    return result
};