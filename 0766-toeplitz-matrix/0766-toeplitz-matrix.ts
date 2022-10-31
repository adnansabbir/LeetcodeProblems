function isToeplitzMatrix(matrix: number[][]): boolean {
    const getValue = (i: number, j: number): number | null => {
        if(i<0 || j<0 || i>= matrix.length || j >= matrix[0].length) return null
        return matrix[i][j]
    }
    
    for(let i = 0; i<matrix.length; i++){
        for(let j = 0; j<matrix[0].length; j++){
            if(getValue(i-1, j-1) === null) continue
            else if(getValue(i-1, j-1) !== matrix[i][j]) return false
        }
    }
    
    return true
};