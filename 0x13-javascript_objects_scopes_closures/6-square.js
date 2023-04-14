#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (typeof c === 'undefined') {
      for (let i = 0; i < this.height; i++) {
        console.log(`${'X'.repeat(this.width)}`);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(`${c.repeat(this.width)}`);
      }
    }
  }
}

module.exports = Square;
