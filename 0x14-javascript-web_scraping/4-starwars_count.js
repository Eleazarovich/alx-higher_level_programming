#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const options = { json: true };

request(url, options, (err, resp, body) => {
  if (err) console.log(err);
  let count = 0;
  for (const film of body.results) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
