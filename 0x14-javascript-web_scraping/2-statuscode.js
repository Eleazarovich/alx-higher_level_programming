#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, resp) => {
  if (err) console.log(err);

  console.log(resp.statusCode);
});
