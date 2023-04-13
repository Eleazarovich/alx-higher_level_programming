#!/usr/bin/node

function factorial (number) {
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

if (process.argv.slice(2).toString() === '') {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
