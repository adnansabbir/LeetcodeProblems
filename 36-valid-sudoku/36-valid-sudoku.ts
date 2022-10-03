function isValidSudoku(board: string[][]): boolean {
    
    const columnsHasUniqueNumbers = (board: string[][])=>{
        const width = board[0].length
        const length = board.length
        
        for(let w = 0; w < width; w++){
            const checked = new Set<string>()
            
            for(let l = 0; l < length; l++){
                if(checked.has(board[l][w])) return false
                else if(board[l][w] !== '.') checked.add(board[l][w])
            }
        }
        
        return true
    }
    
    const rowsHasUniqueNumbers = (board: string[][])=>{
        const width = board[0].length
        const length = board.length
        
        for(let l = 0; l < length; l++){
            const checked = new Set<string>()
            
            for(let w = 0; w < width; w++){
                if(checked.has(board[l][w])) return false
                else if(board[l][w] !== '.') checked.add(board[l][w])
            }
        }
        return true
    }
    
    const segmentHasUniqueNumbers = (size: number, board: string[][]) => {
        for(let sr = 0; sr < size; sr++){
            for(let sc = 0; sc < size; sc++){
                const checked = new Set<string>()
                for(let r = sr*size; r< (sr*size)+size; r++){
                    for(let c = sc*size; c < (sc*size) + size; c++){
                        if(checked.has(board[r][c])) return false
                        else if(board[r][c] !== '.') checked.add(board[r][c])
                    }
                }
                
            }    
        }
        
        return true
    }
    
    return columnsHasUniqueNumbers(board) && rowsHasUniqueNumbers(board) && segmentHasUniqueNumbers(3, board)
    
};