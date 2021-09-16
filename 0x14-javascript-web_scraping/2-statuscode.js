#!/usr/bin/node

const request = require('request');

request(process.argv[2],(error, data) => {
  if (error) {
    console.log('code:', error);
  } else {
    console.log('code:', data.statusCode);
  }
});
