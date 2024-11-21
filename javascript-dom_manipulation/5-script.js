const updateHeaderButton = document.getElementById('update_header');
const header = document.getElementById('header');
updateHeaderButton.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
});
