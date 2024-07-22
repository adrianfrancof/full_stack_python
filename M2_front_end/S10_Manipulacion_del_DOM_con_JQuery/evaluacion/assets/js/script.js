$(document).ready(function() {
    $(".text-body-secondary").click(function() {
      var idBoton = $(this).attr("id"); //this obtiene el evento y de ese evento el id, lo guarda
      $("#detalles" + idBoton).toggle(); //detallesBaires, detallesMachupichu, se concatena detalles+id
    });


    $(".btn-close").click(function() {
        $(".detalles").hide(); //se cambio el efecto de show() a hide()
    });
  });