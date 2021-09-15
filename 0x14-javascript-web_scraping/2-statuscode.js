#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, data) {
  if (error) {
    console.log('code:', error);
  }
  console.log('code:', data.statusCode);
});
