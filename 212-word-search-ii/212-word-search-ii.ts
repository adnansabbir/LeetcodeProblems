function findWords(board: string[][], words: string[]): string[] {
    // if word length is more than total char in board it is not there
    const M = board.length, N = board[0].length
    const wordMap = new Set<string>(words)
    const result = []
    let maxWordLength = Math.max(...words.map(w => w.length))


    const colllectWordsFromBoard = (row: number, col: number, currWord: string, avoid = new Set<string>()): void => {
        if(row<0 || col<0 || row>=M || col>=N || currWord.length === maxWordLength) return
        const key = `${row}-${col}`
        if(avoid.has(key)) return

        avoid.add(key)
        currWord += board[row][col]
        if(wordMap.has(currWord)){
            result.push(currWord)
            wordMap.delete(currWord)
        }
        colllectWordsFromBoard(row+1, col, currWord, avoid)
        colllectWordsFromBoard(row-1, col, currWord, avoid)
        colllectWordsFromBoard(row, col+1, currWord, avoid)
        colllectWordsFromBoard(row, col-1, currWord, avoid)
        avoid.delete(key)
    }

    for(let i = 0; i<M; i++){
        for(let j=0; j<N; j++){
            colllectWordsFromBoard(i, j, "")
        }
    }

    return result
};