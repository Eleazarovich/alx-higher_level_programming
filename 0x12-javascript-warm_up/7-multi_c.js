#!/usr/bin/node

if (parseInt(process.argv[2])) {
  const n = parseInt(process.argv[2]);
  if (n > 0) {
    for (let i = 0; i < n; i++) {
      console.log('C is fun');
    }
  } else {
    // do nothing
  }
} else {
  console.log('Missing number of occurrences');
}
