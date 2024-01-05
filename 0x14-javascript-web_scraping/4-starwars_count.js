#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, code, body) => {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    for (const film in JSON.parse(body).results) {
      for (const character in JSON.parse(body).results[film].characters) {
        if (JSON.parse(body).results[film].characters[character].includes('18')) { count += 1; }
      }
    }
    console.log(count);
  }
});
