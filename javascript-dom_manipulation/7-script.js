async function title_(){
    const ul = document.getElementById('list_movies');
    const response = await (await fetch('https://swapi-api.hbtn.io/api/films/?format=json')).json();
    const results = response["results"] // value
    for (search = 0; search < response['count']; search++){
        const newelement = document.createElement('li')
        newelement.textContent = results[search]['title']
        ul.appendChild(newelement);
    }
}
title_()