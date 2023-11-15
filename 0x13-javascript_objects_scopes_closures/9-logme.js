#!/usr/bin/node

exports.logMe = function (item) {
  if (!exports.logList) {
    exports.logList = {};
  }
  const count = Object.keys(exports.logList).length;
  exports.logList[count] = item;

  const latestKey = count.toString();
  console.log(`${latestKey}: ${exports.logList[latestKey]}`);
};
