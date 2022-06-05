/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    let result = 0
    const queens = new Array(n).fill(0).map(_ => new Array(n).fill('.'))
    
    const placeQueens = (row, bookedCols, bookedPosD, bookedNegD) => {
        
        for(let i = 0; i < n; i++){
            const col = i
            const posD = row + i
            const negD = row - i
            
            if(bookedCols.has(col) || bookedPosD.has(posD) || bookedNegD.has(negD)) continue
            
            queens[row][i] = "Q"
            
            if(row === n - 1){
                result++
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