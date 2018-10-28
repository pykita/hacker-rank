'use strict';

function isMagicSquare(square) {
    const arr = [];
    const rowSums = [0, 0, 0];
    const columnSums = [0, 0, 0];
    const diagonalSum = [0, 0];
    for (let i = 0; i < square.length; i++) {
        for (let j = 0; j < square[i].length; j++) {
            rowSums[i] += square[i][j];
            columnSums[i] += square[i][j];

            if (i == j) {
                diagonalSum[0] += square[i][j];
            }

            if (i + j == (square.length - 1)) {
                diagonalSum[1] += square[i][j];
            }
        }
    }
}

function formingMagicSquare(s) {


}

function main() {
    const s = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 5]
    ];

    console.log(isMagicSquare(s));

    const result = formingMagicSquare(s);

    console.log(result);
}

main();
