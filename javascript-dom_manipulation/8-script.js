document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => response.json())
      .then(data => {
        const translatedHello = data.hello;
        document.getElementById('hello').textContent = translatedHello;
      })
      .catch(error => {
        document.getElementById('hello').textContent = 'Failed to load translation.';
        console.error('Error fetching translation:', error);
      });
  });
  