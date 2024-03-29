#!/usr/bin/node
const request = require('request');
const id = '18';
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    let count = 0;
    for (const movies of JSON.parse(body).results) {
      for (const characters of movies.characters) {
        if (characters.includes(id)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
