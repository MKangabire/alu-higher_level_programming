#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
module.exports = Rectangle;
