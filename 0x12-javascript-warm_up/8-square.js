#!/usr/bin/node
const x = process.argv[2];
if (isNaN(parseInt(x))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= parseInt(x); i++) {
    let result = '';
    for (let j = 1; j <= parseInt(x); j++) {
      result = result + 'X';
    }
    console.log(result);
  }
}
