

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
        let filas = table.getElementsByTagName("tr");
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
        td2.appendChild(document.createTextNode(autorCancion.value));
        tr.appendChild(td2);

        let td3 = document.createElement("td");
        let btn = document.createElement("button");
        btn.setAttribute("class","waves-effect waves-red btn modal-trigger red cancion");
        
        let i = document.createElement("i");
        i.setAttribute("class","material-icons");
        i.appendChild(document.createTextNode("delete"))
        btn.appendChild(i);
        td3.appendChild(btn);
        tr.appendChild(td3)


        table.getElementsByTagName("tbody")[0].appendChild(tr);
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


eliminarCancion = (elemento) => {

    let idCancionSucio  = elemento.getAttribute("data-id");
    console.log(idCancionSucio)
    idCancionSucio2 = idCancionSucio.split("-");

    let idCancionLimpio = idCancionSucio2[1]

    console.log(idCancionLimpio)
    let token = getCookie('csrftoken');

    $.ajax({

        type:"POST",
        url:"http://localhost:8000/artista/DeleteCancion",
        data : {

                csrfmiddlewaretoken : token,
                idCancion  : idCancionLimpio

        },
        success : function(data){
            // alert(data);

            document.getElementById(idCancionSucio).innerHTML = "";
        },
        error: function(data){
            console.log(data)
            alert("Ha ocurrido un error")
        }

    })

}

editarCancion = (elemento) => {

let idElementoTr = elemento.getAttribute("data-id");
let elementoTR = document.getElementById(idElementoTr)


let btnEditar = document.getElementById("btn-editar-"+idElementoTr);
btnEditar.textContent="save";
btnEditar.removeAttribute("onclick");
btnEditar.onclick = function(){

    actualizarCancion(idElementoTr);
    
    
}

let btnEliminar = document.getElementById("btn-eliminar-"+idElementoTr);
btnEliminar.textContent="cancel";
btnEliminar.removeAttribute("data-toggle");
btnEliminar.removeAttribute("href");
btnEliminar.classList.remove("model-trigger")
btnEliminar.onclick = function(){

    cancelarActualizarCancion(idElementoTr);
}

for(let x = 1 ;x<3 ; x++){
    
    elementoTR.children[x].classList.add("editable")
    elementoTR.children[x].setAttribute("contenteditable","true")
    // elementoTR.children[x].classList.add("form-control-sm")
}
}

actualizarCancion = (id) => {
   
  
    idCancionSucio2 = id.split("-");

    let idCancionLimpio = idCancionSucio2[1];
  
    let elementoTR = document.getElementById(id)
    
    let token = getCookie('csrftoken');
    $.ajax({

        type:"POST",
        url:"http://localhost:8000/artista/Update",
        data : {

                csrfmiddlewaretoken : token,
                idCancion  : idCancionLimpio,
                nombreCancion : elementoTR.children[1].textContent,
                autorCancion : elementoTR.children[2].textContent

        },
        success : function(data){
            // alert(data);

        },
        error: function(data){
            console.log(data)
            alert("Ha ocurrido un error")
        }

    })
}


cancelarActualizarCancion = (idElementoTr) => {
  
    let elementoTR = document.getElementById(idElementoTr)
    
    
    let btnEditar = document.getElementById("btn-editar-"+idElementoTr);
    btnEditar.textContent="create";
   
    btnEditar.onclick = function(){
    
        editarCancion(btnEditar);
        
        
    }
    
    let btnEliminar = document.getElementById("btn-eliminar-"+idElementoTr);
    btnEliminar.textContent="delete";
    
    btnEliminar.removeAttribute("onclick");
    
    
    
    for(let x = 1 ;x<3 ; x++){
        
        elementoTR.children[x].classList.remove("editable")
        // elementoTR.children[x].classList.add("form-control-sm")
    }
setTimeout(function(){
    btnEliminar.setAttribute("href","#ModalEliminar")
    btnEliminar.classList.add("model-trigger")
},1000)

}


agregarAlbum = () => {

   

    let nombreAlbum = document.getElementById('NombreAlbum');
    let fechaAlbum = document.getElementById('FechaAlbum');
    let disqueraAlbum  = document.getElementById('disqueraAlbum');
    let generoAlbum = document.getElementById('generoAlbum');
    let fotoAlbum = document.getElementById('fotoAlbum');

    let formData = new FormData();
    formData.append("csrfmiddlewaretoken",getCookie('csrftoken'));
    formData.append("nombreAlbum",nombreAlbum.value);
    formData.append("fechaAlbum",fechaAlbum.value);
    formData.append("disqueraAlbum",disqueraAlbum.value);
    formData.append("generoAlbum",generoAlbum.value);
    formData.append("fotoAlbum",fotoAlbum.files[0]);


    let numeroCanciones = 0
    
    $.each($("#cancionesAlbum"),function(i,obj){
        $.each(obj.files,function(j,file){

            numeroCanciones = j 
            console.log(numeroCanciones)
            formData.append('cancion['+j+']',file);
            console.log('cancion['+j+']');
        })
    })

    formData.append("numeroCanciones", numeroCanciones.toString());

    $.ajax({

        type:"POST",
        url:"http://localhost:8000/artista/AlbumAdd",
        data: formData,
        
        processData : false,
        contentType  : false,
        success: function(data){
            console.log(data)

            const elem = document.getElementById('ModalExito');
            const instance = M.Modal.init(elem);
            instance.open();

            nombreAlbum.value = "";
            fechaAlbum.value = "";
            disqueraAlbum.value = "";
            fotoAlbum.value = "";
            generoAlbum.value = "";
            document.getElementById("cancionesAlbum").value = "";
            document.getElementById("cancionesAlbumtxt").value = "";
            document.getElementById("fotoAlbumImg").value = "";
        },
        error:function(data){
            console.log(data)
        }



});
}

buscarCancion = () =>{

    let texto = document.getElementById("search").value;
    let token = getCookie('csrftoken');

    $.ajax({
        type : 'POST',
        url : 'http://localhost:8000/Usuarios/busqueda',
        data : {

            csrfmiddlewaretoken : token,
            texto : texto 
        },
        success : function(data){
            tablaCanciones(data)
            console.log(data)

        },
        error : function(data){
            alert("Ha ocurrido un error")
            console.log(data)
        }


    })
}


tablaCanciones = (data)=>{

let datos = data['lista'];

divPadre = document.getElementById('albums')
divPadre.innerHTML = ""

let tabla = document.createElement("table");
let thead = document.createElement("thead");
let tbody = document.createElement("tbody");
tabla.appendChild(thead)
tabla.appendChild(tbody)

tr1 = document.createElement("tr")
thead.appendChild(tr1)

th1 = document.createElement("th");
th1.appendChild(document.createTextNode("#"))
th2 = document.createElement("th");
th2.appendChild(document.createTextNode("Reproducir"))
th3 = document.createElement("th");
th3.appendChild(document.createTextNode("Nombre"))
th4 = document.createElement("th");
th4.appendChild(document.createTextNode("Autor"))
th5 = document.createElement("th");
th5.appendChild(document.createTextNode("Album"))


tr1.appendChild(th1);
tr1.appendChild(th2);
tr1.appendChild(th3);
tr1.appendChild(th4);
tr1.appendChild(th5);

thead.appendChild(tr1)

for(let x = 0;x<datos.length;x++){


    let tr = document.createElement("tr");

    let th6 = document.createElement("th");
    th6.appendChild(document.createTextNode(x+1));

    let td1 = document.createElement("td");
    let inputMusica = document.createElement("audio");
    inputMusica.setAttribute("preloads","auto");
    inputMusica.setAttribute("controls","true");
    inputMusica.setAttribute("type","audio/mp3");
    let sourceMusica = document.createElement("source");
    sourceMusica.setAttribute("src","/media/"+datos[x][4])
    inputMusica.appendChild(sourceMusica);
    td1.appendChild(inputMusica);

    let td2 = document.createElement("td");
    td2.appendChild(document.createTextNode(datos[x][0]))

    let td3 = document.createElement("td");
    td3.appendChild(document.createTextNode(datos[x][2]))

    let td4 = document.createElement("td");
    td4.appendChild(document.createTextNode(datos[x][3]))

    tr.appendChild(th6);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);

    tbody.appendChild(tr)
    

}

    divPadre.appendChild(tabla)
}