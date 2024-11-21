const toggleHeaderButton = document.getElementById('toggle_header');
toggleHeaderButton.addEventListener('click', function() {
  const header = document.querySelector('h1');
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});