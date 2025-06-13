function setMatrixZeroes(matrix: number[][]) {
    const row_size = matrix.length;
    const col_size = matrix[0].length;

    const rowsToZero: boolean[] =  new Array(row_size).fill(false);
    const colsToZero: boolean[] = new Array(col_size).fill(false);

    // find rows and cols that needs to be zeroed
    for (let row=0; row<row_size; row++) {
        for (let col=0; col<col_size; col++) {
            if (matrix[row][col] === 0){
                rowsToZero[row] = true;
                colsToZero[col] = true;
            }
        }
    }

    // set all cols to zero if a row has zero
    for (let row=0; row<rowsToZero.length; row++){
        if (rowsToZero[row]){
            // set all cols to zero
            for (let col=0; col<col_size; col++){
                matrix[row][col] = 0;
            }
        } 
    }

    // set all rows to zero if a col has a zero
    for (let col=0; col<colsToZero.length; col++){
        if (colsToZero[col]){
            // set all rows to zero
            for(let row=0; row< row_size; row++){
                matrix[row][col] = 0;
            }
        }
    }
}

const input2: number[][] = [[1,1,1],[1,0,1],[1,1,1]];
console.log(input2);
setMatrixZeroes(input2);
console.log(input2);