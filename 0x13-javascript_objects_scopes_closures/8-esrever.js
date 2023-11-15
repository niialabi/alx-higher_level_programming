#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const newList = [];
  for (let i = 0; i < len; i++) {
    newList[i] = list[len - 1 - i];
  }
  return newList;
};
