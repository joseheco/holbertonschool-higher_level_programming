#!/usr/bin/node

const request = require('request');

request(process.argv[2], { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let completed = {};
    for (let todo of body) {
      if (todo.completed === true) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 0;
        }
        completed[todo.userId]++;
      }
    }
    console.log(completed);
  }
});
