const botton = document.getElementById('add_item');
const list = document.querySelector('.my_list');

botton.addEventListener('click', function(){

    const newelement = document.createElement('li');
    newelement.textContent = 'Item';
    
    list.appendChild(newelement);
});

