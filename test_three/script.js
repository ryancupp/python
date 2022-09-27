console.log('Script attached good to go')
URL = 'https://pokeapi.co/api/v2/pokemon/'


function getPoke(event) {
    event.preventDefault()
    console.log("Submitted")
    const pokeResultDiv = document.querySelector("#pokeResult")
    pokeResultDiv.innerHTML = "Loading......"
    const pokeName = document.querySelector("#pokeName").value
    console.log(pokeName)
    fetch(URL + pokeName)
        .then(res => res.json())
        .then(poke => {
            console.log(poke)
            pokeResultDiv.innerHTML = `
            <h3>Number ${poke.id} ${poke.name}</h3>
            <img src="${poke.sprites.front_default}">
            `
            for (type of poke.types) {
                console.log(type)
                pokeResultDiv.innerHTML += `<p>${type.type.name}</p>`
            }
        })
        .catch(err => console.log(err))

}


async function getRandom(event) {
    const pokeResultDiv = document.querySelector("#pokeResult")
    let rand = Math.floor(Math.random() * 905)
    let response = await fetch(URL + rand)
    let poke = await response.json()
    pokeResultDiv.innerHTML = `
            <h3>Number ${poke.id} ${poke.name}</h3>
            <img src="${poke.sprites.front_default}">
            `
    for (type of poke.types) {
        console.log(type)
        pokeResultDiv.innerHTML += `<p>${type.type.name}</p>`
    }


}