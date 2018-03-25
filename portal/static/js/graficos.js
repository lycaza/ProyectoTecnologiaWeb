function basic_pie(container,v) {
 
  var
    d1 = [[0, 1]],   
    d2 = [[0, v*1]],
    graph;
  
  graph = Flotr.draw(container, [
    { data : d1, label : 'Egresos' },
    { data : d2, label : 'Ingresos' }
   
  ], {
    HtmlText : false,
    
    grid : {
      verticalLines : false,
      horizontalLines : false,
    },
    xaxis : { showLabels : false },
    yaxis : { showLabels : false },
    pie : {
      show : true, 
      explode : 6
    },
    mouse : { track : true },
    legend : {
      position : 'se',
      backgroundColor : '#D2E8FF'

    }
  });
};