
//reference to the "header" element
const header = document.querySelector('header');

//reference to the "#toggle_header" element
const toggleHeader = document.querySelector('#toggle_header');

toggleHeader.addEventListener('click', function() {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else {
    header.classList.remove('red');
    header.classList.add('green');
  }
});