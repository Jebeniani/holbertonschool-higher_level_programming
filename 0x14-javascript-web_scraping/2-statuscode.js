#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response) {
  if (err) {
    console.error('err', err);
  } else {
    console.log('code:', response.statusCode);
  }
});
