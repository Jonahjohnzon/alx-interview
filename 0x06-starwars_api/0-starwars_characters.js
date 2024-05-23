#!/usr/bin/node

// Import 'request' library
const request = require('request');

// Define constant with base URL of Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if the number of command line arguments is greater than 2
if (process.argv.length > 2) {
  // Make a request to film resource for the specified film ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // If an error occurred during the request, log the error
    if (err) {
      console.log(err);
    }
    // Get characters URL from the film's response body
    const charactersURL = JSON.parse(body).characters;

    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Make a request to the character resource
        request(url, (promiseErr, __, charactersReqBody) => {
          // If an error occurred during the request, reject the Promise with the error
          if (promiseErr) {
            reject(promiseErr);
          }
          // Resolve the Promise with the name of the character
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // Wait for all Promises to resolve
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
