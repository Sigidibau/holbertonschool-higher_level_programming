const redHeaderButton = document.getElementById('red_header');

redHeaderButton.addEventListener('click', function() {
  const header = document.querySelector('h1');
  header.style.color = '#FF0000';
});
