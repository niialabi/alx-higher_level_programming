#!/usr/bin/node
const Square5 = require('./5-square.js');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    // if c is undefined us x instead
    if (c === undefined) {
      c = 'X';
    }
    let printResult = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        printResult += c;
      }
      console.log(printResult);
      printResult = '';
    }
  }
}
module.exports = Square;
