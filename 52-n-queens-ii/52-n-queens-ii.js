/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    let result = 0
    const placeQueens = (row, bookedCols, bookedPosD, bookedNegD) => {
        
        for(let i = 0; i < n; i++){
            const col = i
            const posD = row + i
            const negD = row - i
            
            if(bookedCols.has(col) || bookedPosD.has(posD) || bookedNegD.has(negD)) continue
            
            if(row === n - 1){
                result++
                continue
            }
            
            bookedCols.add(col)
            bookedPosD.add(posD)
            bookedNegD.add(negD)
            
            placeQueens(row + 1, bookedCols, bookedPosD, bookedNegD)
            
            bookedCols.delete(col)
            bookedPosD.delete(posD)
            bookedNegD.delete(negD)
        }
    }
    
    placeQueens(0, new Set(), new Set(), new Set())
    
    return result
};