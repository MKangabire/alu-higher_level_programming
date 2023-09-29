#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const { argv } = require('process');
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

if (!isNaN(num1) && !isNaN(num2)) {
  const result = add(num1, num2);
  console.log(result);
} else {
  console.log('NaN');
}
