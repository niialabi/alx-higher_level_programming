#!/usr/bin/node

const args = process.argv;
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

request('https://swapi-api.alx-tools.com/api/films/' + args[2],
  async function test (error, code, body) {
    if (error) {
      console.error(error);
    } else {
      for (const character of JSON.parse(body).characters) {
        try {
          const response = await requestPromise(character, { json: true });
          console.log(response.body.name);
        } catch (err) {
          console.log(err);
        }
      }
    }
  });
