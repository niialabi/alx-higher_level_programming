#!/usr/bin/node
const { argv } = require('process');
if (isNaN(Number.parseInt(argv[2], 10))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number.parseInt(argv[2], 10)}`);
}
