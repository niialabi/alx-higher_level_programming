#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) { console.log('0'); } else {
  const arr = argv.slice(2);
  arr.sort((x, y) => (Number.parseInt(y, 10) - Number.parseInt(x, 10)));
  console.log(arr[1]);
}
