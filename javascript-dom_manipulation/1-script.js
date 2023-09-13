// referencia al elemento de cabecera por su id
const change_color = document.getElementById("red_header")

// Adds the click to the header element
change_color.addEventListener('click', function(){
    document.querySelector('header').style.color = '#FF0000'
})
