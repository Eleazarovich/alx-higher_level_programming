#!/usr/bin/node

if (process.argv.slice(2).toString() === '') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
