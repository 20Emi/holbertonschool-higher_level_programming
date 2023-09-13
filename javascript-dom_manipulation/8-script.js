async function name_(){
    const response = await (await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')).json();
    document.querySelector('#hello').innerHTML = response['hello']
}
name_() // llama a la función