//reference to the header element by its id
var header = document.getElementById('update_header');
// Adds the click to the header element
header.addEventListener('click', function(){
    header.textContent = 'New Header!!!';
})