#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const options = { json: true };

request(url, options, (err, resp, body) => {
  if (err) console.log(err);
  console.log(body.title);
});
