#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

if (argv[2]) {
  fs.readFile(argv[2], 'utf-8', (err, data) => {
    if (err) {
      console.error('An error occurred while reading the file:', err);
    } else {
      console.log(data);
    }
  });
} else {
  console.error('Usage: ./script-name.js <file-path>');
  process.exit(1); // Exit with an error code}
