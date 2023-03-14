#!/usr/bin/node
class Square extends require('./5-square.js') {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let row = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      row += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
