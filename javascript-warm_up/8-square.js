#!/usr/bin/node
const { argv } = require('process');
const squaresize = parseInt(argv[2]);

if (isNaN(squaresize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squaresize; i++) {
    console.log('X'.repeat(squaresize));
  }
}
