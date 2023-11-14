#!/usr/bin/node
function compFactorial (i) {
  if (i === 0 || i === 1) {
    return (1);
  } else {
    return (i * compFactorial(i - 1));
  }
}
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(compFactorial(Number.parseInt(argv[2], 10)));
}
