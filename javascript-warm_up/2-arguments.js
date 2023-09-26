#!/usr/bin/node

function print (sentence) {
  if (sentence === undefined) {
    console.log('No argument');
  } else {
    console.log(sentence);
  }
}

const args = process.argv.slice(2);

if (args.length === 0) {
  print();
} else if (args.length === 1) {
  print('Argument found');
} else {
  print('Arguments found');
}
