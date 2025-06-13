/*
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
*/
function setZeroes(matrix: number[][]) {

    const row_size = matrix.length;
    const column_size = matrix[0].length;
    const zeroLocation: Map<string, boolean> = new Map<string, boolean>();
    
    // get location of all the zeroes
    for(let row=0; row<row_size; row++){
        for(let column=0; column<column_size; column++ ){
            if(matrix[row][column] === 0){
                zeroLocation.set(`${row}-${column}`, true);
                console.log(`found at row:${row} and column:${column}`);
            }
        }
    }

    // print all elements matrix
    console.log("matrix: ",matrix);
    
    // start setting zeroes
    zeroLocation.forEach((value, key) => {
        const [row, column] = key.split("-").map(Number);
        
        // move right
        for(let curr_column=column; curr_column<column_size; curr_column++){
            matrix[row][curr_column] = 0;
        }

        // move left
        for(let curr_column=column; curr_column>=0; curr_column--){
            matrix[row][curr_column] = 0;
        }

        // move up
        for(let currRow=row; currRow>=0; currRow--){
            matrix[currRow][column] = 0;
        }
        
        // move down
        for(let currRow=row; currRow<row_size; currRow++){
            matrix[currRow][column] = 0;
        }


    });
    console.log("matrx after: ", matrix);
    
};

const input1 = [[1,1,1],[1,0,1],[1,1,1]];
setZeroes(input1);