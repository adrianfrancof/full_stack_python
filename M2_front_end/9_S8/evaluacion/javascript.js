// Cada uno de los clientes de nuestro banco contará con un nombre, 
// un identificador, una clave y un saldo en su cuenta.
// Se debe contar con al menos 3 clientes registrados.

// nombre | rut | clave | saldo
//funcion constructora para instanciar objeto Cliente
function Cliente(nombre, rut, clave, saldo) {
    this.nombre = nombre
    this.rut = rut
    this.clave = clave
    this.saldo = saldo
}

// declaracion para crear un objeto cliente
var cliente1 = new Cliente("Fulanito Perez", "270000001", "0000", 100000)
var cliente2 = new Cliente("Maria Delgado", "270000002", "0001", 200000)
var cliente3 = new Cliente("Jose Feliciano", "270000003", "0002", 300000)

var listaClientes = [cliente1, cliente2, cliente3] //lista para recorrer y buscar

//Cuando se ingrese el identificador y la clave, 
// se revisará si coincide con alguno de los clientes registrados. 
// Si no coincide, se mostrará un mensaje de error.

alert("Bienvenido a Banca en Línea")
var identificador = prompt("Ingrese su identificador") // ingreso de valores
var password = prompt("Ingrese su password") // ingreso de valores

// recorrer la lista con clientes
var usuario;
for (const iterator of listaClientes) {
    if (iterator.rut === identificador && iterator.clave === password) {
        usuario = iterator; //cliente existe
        break;
    }
}

// var usuario;
// for (let index = 0; index < listaClientes.length; index++) {
//     if(listaClientes[index].rut === identificador && listaClientes[index].clave === password){
//         usuario = listaClientes[index]
//         break;
//     } 
// }

//validacion si el usuario fue encontrado
if (usuario) {
    alert("Bienvenido " + usuario.nombre)
    menu(usuario) //llamada a funcion menu cuando el cliente existe 
}else {
    alert("Datos incorrectos")
}

// funcion menu
function menu(usuario) { //"Seleccione que desea hacer: 1.- Ver saldo. 2.- 3.-"
    do {
        var opcion = prompt("Seleccione que desea hacer:\n"+
            "1.- Ver saldo.\n" +
            "2.- Realizar giro\n" +
            "3.- Realizar deposito\n" +
            "4.- Salir"
        )

        switch (opcion) {
            case "1": //ver saldo
                alert("Su saldo es: " + usuario.saldo)
                break;
            case "2": //realizar deposito
                break;
            case "3":
                break    
            case "4":
                break;
            default:
                break;
        }
    } while (opcion != "4");
}


