const redHeaderButton = document.getElementById('red_header');
redHeaderButton.addEventListener('click', function() {
  const header = document.querySelector('header');
  header.classList.add('red');
});
