/*
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
*/

function minDistance(word1: string, word2: string): number {
    let i = word1.length - 1;
    let j = word2.length - 1 ;
    let dp: number[][] = [];
    for (let row=0; row<=i; row++){
        dp[row] = new Array(j+1).fill(-1);
    }
    return getMinDistance(i, j, word1, word2, dp);

};

function getMinDistance(i: number, j: number, word1: string, word2: string, dp: number[][]): number{
    let insertOp: number;
    let deleteOp: number; 
    let replaceOp: number;

    if (i === -1){
        return j + 1;
    } else if (j === -1){
        return i + 1;
    }

    if (dp[i][j] !== -1) return dp[i][j];

    if (word1[i] === word2[j]) {
        return dp[i][j] = getMinDistance(i-1, j-1, word1, word2,dp);
    } else {
        insertOp = 1 + getMinDistance(i, j-1, word1, word2,dp);
        deleteOp = 1 + getMinDistance(i-1, j, word1, word2,dp);
        replaceOp = 1 + getMinDistance(i-1, j-1, word1, word2,dp);

        return dp[i][j] = Math.min(insertOp, deleteOp, replaceOp);
    }
};