// Fetch the data from the URL using the Fetch API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())  // Convert the response to JSON
  .then(data => {
    // Extract the character name from the response data
    const characterName = data.name;

    // Display the character name in the HTML element with id 'character'
    document.getElementById('character').textContent = characterName;
  })
  .catch(error => {
    // If there's an error (e.g., network failure), display an error message
    document.getElementById('character').textContent = 'Failed to load character data.';
    console.error('Error:', error);
  });
