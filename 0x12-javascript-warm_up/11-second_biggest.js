#!/usr/bin/node

const argument = process.argv;
if (isNaN(parseInt(argument[2])) || isNaN(parseInt(argument[3]))) {
  console.log(0);
} else {
  const argLength = process.argv.length;
  const sliced = process.argv.slice(2, argLength);
  const sorted = sliced.sort(function (a, b) { return a - b; });
  const sortedLen = sorted.length;
  console.log(sorted[sortedLen - 2]);
}
