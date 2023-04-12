#!/usr/bin/node

const n = process.argv.length;

if (n < 3) {
  console.log('No argument');
} else if (n < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
