#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (let result of body.results) {
      for (let character of result.characters) {
        if (character.endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
