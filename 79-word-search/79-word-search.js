/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    let visited = new Set()
    const foundWord = (x, y, idx) => {
        if(
            visited.has(`${x}-${y}`) || 
            x < 0 || 
            x >= board.length || 
            y < 0 || 
            y >= board[0].length || 
            board[x][y] !== word[idx]) return false
        
        
        visited.add(`${x}-${y}`)
        if(
            idx === word.length - 1 ||
            foundWord(x-1, y, idx + 1) ||
            foundWord(x+1, y, idx + 1) ||
            foundWord(x, y - 1, idx + 1) ||
            foundWord(x, y + 1, idx + 1)
        ) {
            visited.delete(`${x}-${y}`)
            return true
        }
        visited.delete(`${x}-${y}`)
        return false
    }
    
    for(let i = 0; i<board.length; i++){
        for(let j = 0; j < board[0].length; j++){
            if(board[i][j] === word[0]){
                if(foundWord(i, j, 0)) return true
            }
        }
    }
    
    return false
};