
function inicio(){
	location.href= "login"; 
}


function login(){
	var usuario = $("#usuario").val();
	var contrasenia = $("#clave").val(); 
				
	if(usuario!="" & contrasenia!="")
		location.href="inicio";
	else
		alert("Ingrese usuario y contraseña");
}


function mostrarMapa(){
	// Creamos el punto a partir de las coordenadas:
	var punto = new google.maps.LatLng(-2.0297827,-79.913673);
	 
	// Configuramos las opciones
	var myOptions = {
	    zoom: 15, center: punto, mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	 
	// Creamos el mapa
	document.getElementById("mapa").innerHTML= "";
	var map = new google.maps.Map(document.getElementById("mapa"),  myOptions);
	 
	// Marcador inicial
	var marker = new google.maps.Marker({
	    position:punto,
	    map: map,
	    title:"Título del mapa"
	});


	punto = new google.maps.LatLng(-2.0328285,-79.9139304);
	marker.push(new google.maps.Marker({
		map: map,
		position: punto,
		title:"Título del mapa"
	}));

	
}

