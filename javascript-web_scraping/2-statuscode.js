#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node get-status-code.js <URL>');
    process.exit(1); // Exit with an error code
}
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1); // Exit with an error code
    }

    console.log(`code: ${response.statusCode}`);
});
