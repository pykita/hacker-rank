'use strict';

const fs = require('fs');

// process.stdin.resume();
// process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

// process.stdin.on('data', inputStdin => {
//     inputString += inputStdin;
// });

// process.stdin.on('end', _ => {
//     inputString = inputString.replace(/\s*$/, '')
//         .split('\n')
//         .map(str => str.replace(/\s*$/, ''));

//     main();
// });

function readLine() {
    return inputString[currentLine++];
}

function drawLines(str) {
    let maxHeight = 0, minHeight = 0;
    const composedStruct = {};
    for (let index = 0; index < str.length; index++) {
        if (str == '/') {
            composedStruct[index.toString()]
        }
        
    }

}

// Complete the countingValleys function below.
function countingValleys(n, s) {
    const toLines = s.replace(/D/g, '\\').replace(/U/g, '/');
    console.log(toLines);
}

function main() {
    // const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    // const n = parseInt(readLine(), 10);

    // const s = readLine();

    let result = countingValleys(8, 'UDDDUDUU');

    // ws.write(result + "\n");

    // ws.end();
}

main()