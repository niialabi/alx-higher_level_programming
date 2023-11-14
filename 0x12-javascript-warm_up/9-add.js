#!/usr/bin/node
function add (i, j) {
  return (Number(i) + Number(j));
}
const { argv } = require('process');
console.log(add(argv[2], argv[3]));
