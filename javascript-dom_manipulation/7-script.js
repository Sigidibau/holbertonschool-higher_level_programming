fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())  // Parse the JSON data from the response
  .then(data => {
    const films = data.results;
    const listElement = document.getElementById('list_movies');
    films.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listElement.appendChild(listItem);
    });
  })
  .catch(error => {
    const listElement = document.getElementById('list_movies');
    listElement.innerHTML = '<li>Failed to load movie titles.</li>';
    console.error('Error:', error);
  });
