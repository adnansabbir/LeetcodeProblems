/**
 * @param {number[][]} matrix
 */
// var NumMatrix = function(matrix) {
// };

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
// NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
// };

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */

class NumMatrix{
    constructor(matrix){
        this.matrix = matrix
        this.fillSum()
    }
    
    sumRegion(x1, y1, x2, y2){
        return this.matrix[x2][y2] - this.getValue(x1-1, y2) - this.getValue(x2, y1-1) + this.getValue(x1-1, y1 - 1)
    }
    
    getValue(x, y){
        return (x >= 0 && y >= 0) ? this.matrix[x][y] : 0
    }
    
    fillSum(){
        for(let x = 0; x < this.matrix.length; x++){
            for (let y = 0; y < this.matrix[0].length; y++){
                this.matrix[x][y] = ((this.getValue(x - 1, y) + this.getValue(x, y - 1)) - this.getValue(x - 1, y - 1)) + this.matrix[x][y]
            }
        }
        console.log(this.matrix)
    }
}