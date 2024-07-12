// \n es salto de linea

var opcion = prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel.\n" + 
    "Estoy aquí para ayudarte en lo que necesites.\n" +
    "Escribe el número de la opción que buscas: \n" +
    "1.- Boletas y Pagos \n" +
    "2.- Señal y llamadas \n" +
    "3.- Oferta comercial  \n" +
    "4.- Otras consultas")

//FUNCIONES
// estructura de control switch case, donde key es el valora evaluar y value los valores para cada caso
switch (opcion) {
    case "1":
        boletasPagos();
        break; // para salir del caso y terminar el switch case
    case "2":
        reportarProblemas();
        break;
    case "3":
        ofertaComercial();
    case "4":
        otrasConsultas();
    default:
        alert("La opción ingresada no es válida.")
        break;
}

function boletasPagos() {
    var ingreso = prompt("Seleccione una opción\n"+
        "1.- Ver boleta\n"+
        "2.- Pagar cuenta"
    )

    if (ingreso == "1") {
        alert("Haga click para descargar su boleta")
    } else if (ingreso == "2"){
        alert("Ustes está siendo transferido. Espere por favor...")
    } else {
        alert("Opción ingresada no es valida")
    }
}

function reportarProblemas() {
    var ingreso = prompt("Seleccione una opción\n"+
        "1.- Problemas con la señal\n"+
        "2.- Problemas con las llamadas"
    )
    if (ingreso == "1" || ingreso == "2") { // si ingreso es igual a 1 o 2
        var comentario = prompt("A continuación escriba su solicitud") 
        alert(`Estimado usuario, su solicitud: ${comentario}`)
        alert("Estimado usuario, su solicitud: " + comentario)
    } else {
        alert("Opción ingresada no es valida")
    }
}

function ofertaComercial() {
    var ingreso = prompt("Mentel tiene una oferta comercial acorde a tus necesidades!\n"+
        "Para conocer más información y ser asesorado personalmente por un ejecutivo.\n"+
        "Escribe SI, si deseas ser contactado por un ejecutivo.\n"+
        "Escribe NO, si no deseas ser contactado."
    )
    //convirtiendo el ingreso a mayuscula toUpperCase()
    var ingresoMayuscula = ingreso.toUpperCase(); 
    if (ingresoMayuscula == "SI") {
        alert("Un ejecutivo contactara con usted")
    } else if (ingresoMayuscula == "NO") {
        alert("Gracias por preferir nuestros servicios")
    } else {
        alert("Opción ingresada no es valida")
    }
}

function otrasConsultas() {
    var ingreso = prompt("A continuación escriba su consulta")
    alert("Estimado usuario, su consulta: " + ingreso +
        " Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos"
    )
}
