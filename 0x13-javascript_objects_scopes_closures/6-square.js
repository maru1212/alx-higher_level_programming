#!/usr/bin/node

const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let result = '';
        for (let j = 0; j < this.width; j++) {
          result = result + 'C';
        }
        console.log(result);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
