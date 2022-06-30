// this is a sodoku thats has conditions 
//if this conditions are met then it returns a boolean value true
// we have to make sure each row and column  has no duplicate .
//and also the boxes,they should not have duplicates.


/**
 * @param {character[] []} board
 * @return {boolean}
 */

 let board = 
 [["5","3",".",".","7",".",".",".","."]
 ,["6",".",".","1","9","5",".",".","."]
 ,[".","9","8",".",".",".",".","6","."]
 ,["8",".",".",".","6",".",".",".","3"]
 ,["4",".",".","8",".","3",".",".","1"]
 ,["7",".",".",".","2",".",".",".","6"]
 ,[".","6",".",".",".",".","2","8","."]
 ,[".",".",".","4","1","9",".",".","5"]
 ,[".",".",".",".","8",".",".","7","9"]]


// we will check all the rows , first and the columns and then all the boxes
var isValidSudoku = function(board) {
 const row  = {};
 const column = {};
 const box = {};
// the i is the number of rows and the j is the number of columns 
 for(let i = 0; i < 9; i++) {
    for(let j = 0; j < 9; j++) {
        const value = board[i][j];
    if(value !== '.') { // over here we check if there are  spaces 
    const boxidx = Math.floor(i/3)*3 + Math.floor(j/3); // we are checking the boxes values 
    if( row[`${i}-${value}`] || column[`${j}-${value}`] ||  box[`${boxidx}-${value}`]) {
      return false;     //we are checking if the values inside are similar if they are similar,
                        //if they are similar return false 
    }
    row[`${i}-${value}`] = true;
    column[`${j}-${value}`] = true;
    box[`${boxidx}-${value}`] = true;
     }

    }
 }

return true;
};


// 1,2 3,4 6,7
// 8,9 2,5 1,3 


