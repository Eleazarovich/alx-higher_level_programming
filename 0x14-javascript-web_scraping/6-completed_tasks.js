#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const options = { json: true };

request(url, options, (err, resp, body) => {
  if (err) console.log(err);
  const todos = body;
  const usersCompleted = {};
  for (const todo of todos) {
    if (todo.completed === true) {
      if (todo.userId in usersCompleted) {
        usersCompleted[todo.userId]++;
      } else {
        usersCompleted[todo.userId] = 1;
      }
    }
  }
  console.log(usersCompleted);
});
