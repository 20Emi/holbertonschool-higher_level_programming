var botton = document.getElementById('add_item');
var list = document.querySelector('.my_list');

botton.addEventListener('click', function(){

    var newelement = document.createElement('li');
    newelement.textContent = 'Item';
    
    list.appendChild(newelement);
});

