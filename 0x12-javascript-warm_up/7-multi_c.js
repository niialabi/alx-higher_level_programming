#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 3 || isNaN(Number.parseInt(argv[2], 10))) {
  console.log('Missing number of occurrences');
} else if (Number.parseInt(argv[2], 10) < 0) {
  console.log('');
} else {
  let i = 0;
  while (i < Number.parseInt(argv[2], 10)) {
    console.log('C is fun');
    i++;
  }
}
