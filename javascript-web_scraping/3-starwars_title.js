const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node star-wars-movie.js <movie-id>');
  process.exit(1); // Exit with an error code
}
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1); // Exit with an error code
  }
  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(`Title: ${movieData.title}`);
  }
  else {
    console.error(`Error: Status code ${response.statusCode}`);
    process.exit(1); // Exit with an error code
  }
});
