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
	barras(document.getElementById("graficas"),false);	
	obtener_ventas_agencias();
	
	mostrarMapa();
}


function valoresAgencia(agencia){ 
	document.getElementById('graficas').className= "recuadro";
	document.getElementById('indicadores').className= "recuadro";	
	radar(document.getElementById('graficas'));
	obtener_indicador(agencia);
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



function barras(container, horizontal) {
	var c1 = [
    	[1,30],
    	[2,15],
    	[3,20],
    	[4,22],
    	[5,12],
       ];
    var c2 = [
    	[1,30],
    	[2,10],
    	[3,20],
    	[4,22],
    	[5,12],
       ];
    var c3 = [
    	[1,30],
    	[2,10],
    	[3,20],
    	[4,22],
    	[5,12],
       ];
   
    
    // var data= obtener_ventas_categoria();
    var data= [
	    { data : c1, label : 'Categoria 1' },
	    { data : c2, label : 'Categoria 2' },
	    { data : c3, label : 'Categoria 3' }
	];

    var graph = Flotr.draw(
	  	container,
	  	data, 
		{
	    	legend : {
	        	backgroundColor : '#D2E8FF', // Light blue 
	        	position : 'ne',/*se-nw*/
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
    var request;    
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
    } 
    else {
        request = new window.ActiveXObject("Microsoft.XMLHTTP");
    }
    
    request.open("GET", "indicador?agencia="+agencia, true);
    request.send();
    
    request.onreadystatechange = function(){
        if (request.readyState == 4 && request.status == 200){
            google.charts.setOnLoadCallback(drawChart(request.responseText*1)); 
        }
    }
}

function drawChart(porcentaje) {

        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          //['Dia '+lbldiaactual, diaactual],
          //['Dias Acum.', diasacum],
          ['(%)', porcentaje]
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