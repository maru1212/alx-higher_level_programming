#!/usr/bin/node
const x = process.argv[2];
if (isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= parseInt(x); i++) {
    console.log('C is fun');
  }
}
