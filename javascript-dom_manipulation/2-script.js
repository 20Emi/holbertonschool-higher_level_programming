const red_header = document.getElementById('red_header');
const header_element = document.querySelector('header');

red_header.addEventListener('click', function(){
    header_element.classList.add('red');
});