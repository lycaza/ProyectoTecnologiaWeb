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



function valoresIniciales(){	
  obtenerAgencias(); // con datos
	obtener_ventas_categorias(false);	// con datos
	obtener_ventas_agencias(); // con datos	
	mostrarMapaInicial();
}


function valoresAgencia(agencia){ 
	document.getElementById('graficas').className= "recuadro";
	document.getElementById('indicadores').className= "recuadro";	

	radar(document.getElementById('graficas'));
	obtener_indicador(agencia); // con datos
	reloadMarkers(agencia);
}



function obtenerAgencias(){
    var request;    
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
    } 
    else {
        request = new window.ActiveXObject("Microsoft.XMLHTTP");
    }
    
    request.open("GET", "obtener_agencias", true);
    request.send();
    
    request.onreadystatechange = function(){
        if (request.readyState == 4 && request.status == 200){
            document.getElementById("tabla_agencias").innerHTML= request.responseText;
        }
    }
}

/**********************************************************************************************************/
/**********************************************************************************************************/
/************************************************GOOGLE MAPS***********************************************/
/**********************************************************************************************************/
/**********************************************************************************************************/
var latitud_inicial = -2.1842396;
var longitud_inicial = -79.8794098;
var punto = ['ESPOL MSIG', latitud_inicial, longitud_inicial, 4];
var myOptions;
var map;
var markers=[];
var contenedor_mapa;
///var inicio_mapa=true;

var arreglo_inicial = [
    ['Espol MSIG XIX', latitud_inicial, longitud_inicial, 1]
];

var arreglo_final = [
    ['Bondi Beach', latitud_inicial, longitud_inicial-0.01, 4]
    , ['Coogee Beach', latitud_inicial, longitud_inicial-0.02, 5]
    , ['Cronulla Beach', latitud_inicial, longitud_inicial-0.03, 3]
    , ['Manly Beach', latitud_inicial, longitud_inicial-0.04, 2]
    ///, ['Espol MSIG XIX', latitud_inicial, longitud_inicial-0.05, 1]
];

function mostrarMapaInicial(){
	// Creamos el punto a partir de las coordenadas:
	contenedor_mapa = document.getElementById("mapa");
	punto = new google.maps.LatLng(latitud_inicial,longitud_inicial);
	 
	// Configuramos las opciones
	myOptions = {
	    zoom: 13
		, center: new google.maps.LatLng(latitud_inicial,longitud_inicial)
		, mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	 
	// Creamos el mapa
	contenedor_mapa.innerHTML= "";
	map = new google.maps.Map(contenedor_mapa,  myOptions);
		
	setMarkers(arreglo_inicial); 
}

function reloadMarkers(agencia) {
 
    // Loop through markers and set map to null for each
    for (var i=0; i<markers.length; i++) {
     
        markers[i].setMap(null);
    }
    
    // Reset the markers array
    markers = [];
    
    // Call set markers to re-add markers
    ////setMarkers(arreglo_final);
	obtenerClientes(agencia);
}

function setMarkers(locations) {

    for (var i = 0; i < locations.length; i++) {
        var beach = locations[i];
        var myLatLng = new google.maps.LatLng(parseFloat(beach[1]), parseFloat(beach[2]));
        var marker = new google.maps.Marker({
			///center: new google.maps.LatLng(0.8673074,-79.8581815),
            position: myLatLng,
            map: map,
            animation: google.maps.Animation.DROP,
            title: beach[0],
            zIndex: beach[3]
        });
        
        // Push marker to markers array
        markers.push(marker);
    }
}

function obtenerClientes(agencia){
    var request;    
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
    } 
    else {
        request = new window.ActiveXObject("Microsoft.XMLHTTP");
    }
    
	
    request.open("GET", "obtener_clientes?agencia="+agencia, true);
    request.send();
    
    request.onreadystatechange = function(){
        if (request.readyState == 4 && request.status == 200){
			var arreglo_final = [];
			var arreglo_final = JSON.parse("[" + request.responseText + "]");
            ///console.log(arreglo_final);
			setMarkers(arreglo_final);
			nuevasPosiciones = {
				zoom: 6
				, center: new google.maps.LatLng(-1.2570576,-78.6567243)
				, mapTypeId: google.maps.MapTypeId.ROADMAP
			};
			map.setOptions(nuevasPosiciones);
        }
    }
}




/**********************************************************************************************************/
/**********************************************************************************************************/
/********************************************FIN GOOGLE MAPS***********************************************/
/**********************************************************************************************************/
/**********************************************************************************************************/

function obtener_ventas_categorias(horizontal){
    var request;    
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
    } 
    else {
        request = new window.ActiveXObject("Microsoft.XMLHTTP");
    }
    
    request.open("GET", "ventas_categorias", true);
    request.send();
    
    request.onreadystatechange = function(){
        if (request.readyState == 4 && request.status == 200){
            barras(document.getElementById("graficas"),horizontal,request.responseText);
        }
    }
}

function barras(container, horizontal,data) { 
	var graph = Flotr.draw(
	  	container,
	  	eval(data.toString()), 
  		{
  	    	legend : {
  	        	backgroundColor : '#D2E8FF', // Light blue 
  	        	position : 'nw',/*se-nw*/
  	    	},
  		    bars : {
  		      show : true,
  		      stacked : true,
  		      horizontal : horizontal,
  		      barWidth : 0.6,
  		      lineWidth : 1	,
  		      shadowSize : 0
  		    },
  		    grid : {
  		      verticalLines : horizontal,
  		      horizontalLines : !horizontal
  		    }
  	  	}
  	);
}



function radar(container) {

  // Fill series s1 and s2.
  var
    s1 = { label : ' Actual', data : [[0, 3], [1, 8], [2, 5], [3, 5], [4, 3], [5, 9]] },  
    s2 = { label : ' Anterior', data : [[0, 8], [1, 7], [2, 8], [3, 2], [4, 4], [5, 7]] },
    graph, ticks;

  // Radar Labels
  ticks = [
    [0, "Statutory"],
    [1, "External"],
    [2, "Videos"],
    [3, "Yippy"],
    [4, "Management"],
    [5, "oops"]
  ];
    
  // Draw the graph.
  graph = Flotr.draw(container, [ s1,s2 ], {
    radar : { show : true}, 
    grid  : { circular : true, minorHorizontalLines : false}, 
    yaxis : { min : 0, max : 10, minorTickFreq : 2}, 
    xaxis : { ticks : ticks}
  });
}




function obtener_ventas_agencias(){
    var request;    
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
    } 
    else {
        request = new window.ActiveXObject("Microsoft.XMLHTTP");
    }
    
    request.open("GET", "ventas_agencias", true);
    request.send();
    
    request.onreadystatechange = function(){
        if (request.readyState == 4 && request.status == 200){
            pie(document.getElementById("indicadores"),request.responseText);
        }
    }
}

function pie(container,data) {    
  graph = Flotr.draw(
  	container, 
    eval(data.toString()),
    {
    HtmlText : false,
    grid : {
      verticalLines : false,
      horizontalLines : false
    },
    xaxis : { showLabels : false },
    yaxis : { showLabels : false },
    pie : {
      show : true, 
      explode : 6
    },
    mouse : { track : true },
    legend : {
      position : 'ne',
      backgroundColor : '#D2E8FF'
    }
  });

}



function obtener_indicador(agencia){
    var request, request_2;    
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
		request_2 = new window.XMLHttpRequest();
    } 
    else {
        request = new window.ActiveXObject("Microsoft.XMLHTTP");
		request_2 = new window.ActiveXObject("Microsoft.XMLHTTP");
    }
    
    request.open("GET", "indicador?agencia="+agencia, true);
	request_2.open("GET", "indicador_2?agencia="+agencia, true);
    request.send();
    request_2.send();
    
    request.onreadystatechange = function(){
		request_2.onreadystatechange = function(){
			//if (request.readySta_te == 4 && request.status == 200){
				google.charts.setOnLoadCallback(drawChart(request.responseText*1, request_2.responseText*1));
			//}
		}
    }
}

function drawChart(porcentaje, porcentaje_2) {

        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['(% Estimado)', porcentaje_2],
          //['Dias Acum.', diasacum],
          ['(% Años)', porcentaje]
        ]);

        var options = {
          width: 400, height: 250,
          redFrom: 0, redTo: 20,
          yellowFrom:20, yellowTo: 75,
          greenFrom:75, greenTo: 100,
          minorTicks: 5
        };

        var chart = new google.visualization.Gauge(document.getElementById('indicadores'));
        chart.draw(data, options);

        /*setInterval(function() {
          data.setValue(0, 1, 40 + Math.round(60 * Math.random()));
          chart.draw(data, options);
        }, 3000);*/
        
}


function cerrar(){		
	var html_txt= "";
	html_txt+= "<tr>";
	html_txt+= "<td width=\"80%\"><div align=\"center\"><ul class=\"lista_ul\"><li class=\"lista_li\">Cerrando Sesi&oacute;n...</li></ul></div></td>";
	html_txt+= "<td width=\"10%\"><div align=\"center\"><img src=\"imagenes/busqueda_animada.gif\" width=\"50\" height=\"50\" ></div></td>";
	html_txt+= "</tr>";
	document.getElementById("div").innerHTML= html_txt;
	
	envioAjax("servlet/SLoad?accion=cerrar",function(){		  
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			window.location.href = '/index';
		}
	});	
	
}