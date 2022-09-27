const form = document.getElementById('form')
const search = document.getElementById('search')
const result = document.getElementById('result')
const replace = document.getElementById('replace')

// Make sure the client is loaded before calling this method.


// api URL ///
const apiURL = 'https://api.lyrics.ovh';

form.addEventListener('submit', e=> {
    e.preventDefault();
    searchValue = search.value.trim();

    if(!searchValue){
        alert("There is nothing to search")
    }
    else{ 
        searchSong(searchValue)
    }
})

// Key up event listner
const searchOnKeyUp =() =>{
    searchValue = search.value.trim();
    searchSong(searchValue)
}
//search song 
async function searchSong(searchValue){
    const searchResult = await fetch(`${apiURL}/suggest/${searchValue}`)
    const data = await searchResult.json();

    // console.log(finaldata)
    showData(data);
}

//display final result in DO
function showData(data){
  
    result.innerHTML = `
   
    <ul class="song-list">
      ${data.data
        .map(song=> `<li>
                    <div>
                        <strong>${song.artist.name}</strong> -${song.title} 
                    </div>
                    <span data-artist="${song.artist.name}" data-songtitle="${song.title}"> get lyrics</span>
                </li>`
        )
        .join('')}
    </ul>
    `;



}




//event listener in get lyrics button
result.addEventListener('click', e=>{
    const clickedElement = e.target;

    //checking clicked elemet is button or not
    if (clickedElement.tagName === 'SPAN'){
        const artist = clickedElement.getAttribute('data-artist');
        const songTitle = clickedElement.getAttribute('data-songtitle');
        
        getrics(artist, songTitle)
    }
})

// Get lyrics for song
async function getrics(artist, songTitle) {
    var request = new XMLHttpRequest();
    const res = await fetch(`${apiURL}/v1/${artist}/${songTitle}`);

    const data = await res.json();
    const lyrics = data.lyrics.replace(/(\r\n|\r|\n)/g, '<br>');
    result.innerHTML = ` 
    <h4 style="margin-bottom:30px;"><strong>${artist}</strong> - ${songTitle}</h4><ul>
    <div data-artist="${artist}" data-songtitle="${songTitle}"> get lyrics</div>
    <p style="margin-top:20px;">${lyrics}</p>
`    
    
}

