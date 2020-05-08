


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


actualizarAlbum = () => {

let idAlbum = document.getElementById("idAlbum").dataset.idalbum;
let FechaAlbum = document.getElementById("FechaAlbum").innerHTML;
let GeneroAlbum = document.getElementById("GeneroAlbum").innerHTML;
let NombreAlbum = document.getElementById("NombreAlbum").innerHTML;
let datos = {
    idAlbum : idAlbum,
    FechaAlbum : FechaAlbum,
    GeneroALbum: GeneroAlbum,
    NombreAlbum : NombreAlbum


}


fetch("http://localhost:8000/artista/ActualizarAlbum",{

method:"POST",
headers:{
   "X-CSRFToken": getCookie("csrftoken"),
    "Accept":"application/json",
    'X-Requested-With':"XMLHttpRequest"
},
body:JSON.stringify(datos),
mode:'cors',
cache:'default',
credentials:'include'
})
.then(
   
    
    respuesta =>{
        console.log(respuesta.text().then(

            function(data){
                console.log(data)
            }
        ))
        
    }
)
.catch(

    function(error){

        alert("Error")
        console.log(error)
    }
);




}
