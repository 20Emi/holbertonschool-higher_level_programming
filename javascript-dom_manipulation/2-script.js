// reference to the header element by its id
const red_header = document.getElementById('red_header');
// reference to the "header" element
const header_element = document.querySelector('header');

// Adds the click to the header element
red_header.addEventListener('click', function(){
    header_element.classList.add('red');
});