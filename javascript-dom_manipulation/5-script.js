//reference to the header element by its id
const headers = document.getElementById('update_header');
// Adds the click to the header element
headers.addEventListener('click', function(){
    const updater = document.querySelector("header");
    updater.textContent = 'New Header!!!';
})