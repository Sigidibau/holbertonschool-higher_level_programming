const redHeaderButton = document.getElementById('red_header');

redHeaderButton.addEventListener('click', function() {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
