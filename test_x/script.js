URL = 'https://api.lyrics.ovh/v1/'

function getLyrics(event){
    event.preventDefault()
    console.log("submitted")
    const lyricResultDiv = document.querySelector("#lyricResult")
    lyricResultDiv.innerHTML = "Loading..."
    const songArtist = document.querySelector("#artist").value
    const songTitle = document.querySelector("#title").value
    console.log(songArtist)
    console.log(songTitle)
    fetch(URL + songArtist + "/" + songTitle)
        .then(res => res.json())
        .then(song => {
            console.log(song)
        })
}