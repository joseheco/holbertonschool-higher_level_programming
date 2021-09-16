#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
    if (error) {
        console.error(error);
    }
    JSON.parse(body).characters.map((char) => {
        request(char, (error, response, body) => {
            if (error) console.log(error);
            console.log(JSON.parse(body).name);
        });
    });
});
