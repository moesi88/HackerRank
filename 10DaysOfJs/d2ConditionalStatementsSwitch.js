'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    // Write your code here
    const a = s.charAt(0);
    let s1 = new Set(['a', 'e', 'i', 'o', 'u']);
    let s2 = new Set(['b', 'c', 'd', 'f', 'g']);
    let s3 = new Set(['h', 'j', 'k', 'l', 'm']);
    let s4 = new Set(['n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']);
    switch (true) {
        case s1.has(a):
            return 'A';
        case s2.has(a):
            return 'B';

        case s3.has(a):
            return 'C';
        case s4.has(a):
            return 'D';

    }

    return letter;
}

