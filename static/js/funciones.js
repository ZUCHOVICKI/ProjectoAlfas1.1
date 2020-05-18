

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
let FechaAlbum = document.getElementById("FechaAlbum").value;
let GeneroAlbum = document.getElementById("GeneroAlbum").value;
let NombreAlbum = document.getElementById("NombreAlbum").value;
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


eliminarAlbum = () =>{

    let idAlbum = document.getElementById("idAlbum").dataset.idalbum;
    fetch("http://localhost:8000/artista/delete",{

method:"POST",
headers:{
   "X-CSRFToken": getCookie("csrftoken"),
    "Accept":"application/json",
    'X-Requested-With':"XMLHttpRequest"
},
body:JSON.stringify(idAlbum),
mode:'cors',
cache:'default',
credentials:'include'
})
.then(
   
    
    respuesta =>{
        console.log(respuesta.text().then(

            function(data){
                console.log(data)


                if(Boolean(data)){
                    alert("Album Eliminado")
                    window.location = "http://localhost:8000/artista/Canciones"
                }
                else{

                    alert("Ha Ocurrido un Error")
                }
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



agregarCancion = () =>{
    
let nombreCancion = document.getElementById('nombreCancion');
let duracionCancion  =document.getElementById('duracionCancion');
let autorCancion =document.getElementById('autorCancion');
let idAlbum = document.getElementById('albumCancion').dataset.idalbum;
let archivoCancion =document.getElementById('archivoCancion').files[0];

 let formData = new FormData();
 formData.append("csrfmiddlewaretoken",getCookie("csrftoken"));
 formData.append("nombreCancion",nombreCancion.value);
 formData.append("duracionCancion",duracionCancion.value);
 formData.append("autorCancion",autorCancion.value);
 formData.append("idAlbum",idAlbum);
 formData.append("archivoCancion",archivoCancion);
$.ajax({

    type:"POST",
    url:"http://localhost:8000/artista/AddCancion",
    data: formData,
    
    processData : false,
    contentType  : false,
    success: function(data){
        console.log(data);
        if(Boolean(data)){
        // $("#modal1").modal('close')
        // $("#ModalExito").modal('open')
        const elem = document.getElementById('ModalExito');
        const instance = M.Modal.init(elem);
        instance.open();

        let table = document.getElementById("idTable");
        let filas = tablas.getElementsByTagName("tr");
        let numeroFilas = filas.length;
        let tr = document.createElement("tr");
        let th = document.createElement("th");
        th.setAttribute("scope","row");
        th.appendChild(document.createTextNode(numeroFilas));
        tr.appendChild(th);

        let td1 = document.createElement("td");
        td1.appendChild(document.createTextNode(nombreCancion.value));
        tr.appendChild(td1);
        let td2 = document.createElement("td");
        td1.appendChild(document.createTextNode(autorCancion.value));
        tr.appendChild(td2);

        table.getElementsByTagName("tbody")[0].appendChild("tr");
            nombreCancion.value= null;
            duracionCancion.value = 0.0;
            document.getElementById("archivoCancion").value = null

    }
    else{

        const elem = document.getElementById('ModalError');
        const instance = M.Modal.init(elem);
        instance.open();
    }
    }
    
}); 




}