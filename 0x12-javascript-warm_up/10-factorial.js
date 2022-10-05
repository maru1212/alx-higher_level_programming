#!/usr/bin/node
function factorial (n) {
  if (isNaN(parseInt(n)) || n === 1) {
    return 1;
  } else if (n > 1) {
    return n * factorial(n - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
