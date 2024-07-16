// Cada uno de los clientes de nuestro banco contará con un nombre, 
// un identificador, una clave y un saldo en su cuenta.
// Se debe contar con al menos 3 clientes registrados.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Llamada a funciones iniciales, que desencadenan la ejecución del programa
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


const listaClientes = crearDatosPrograma()

//Cuando se ingrese el identificador y la clave, 
// se revisará si coincide con alguno de los clientes registrados. 
// Si no coincide, se mostrará un mensaje de error.


const loginResult = login()

// recorrer la lista con clientes
var usuario = busquedaUsuario(loginResult, listaClientes)

//validacion si el usuario fue encontrado
validacionUsuario(usuario)

menu(usuario) //llamada a funcion menu cuando el cliente existe 

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Creación de funciones
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// nombre | rut | clave | saldo
//funcion constructora para instanciar objeto Cliente
function Cliente(nombre, rut, clave, saldo) {
    this.nombre = nombre
    this.rut = rut
    this.clave = clave
    this.saldo = saldo
}

function crearDatosPrograma() {
    // declaracion para crear un objeto cliente
    var cliente1 = new Cliente("Fulanito Perez", "270000001", "0000", 100000)
    var cliente2 = new Cliente("Maria Delgado", "270000002", "0001", 200000)
    var cliente3 = new Cliente("Jose Feliciano", "270000003", "0002", 300000)

    return [cliente1, cliente2, cliente3] //lista para recorrer y buscar
}

function login() {
    alert("Bienvenido a Banca en Línea")
    const inputIdentificador = prompt("Ingrese su identificador");
    const inputPassword = prompt("Ingrese su password");

    return { identificador: inputIdentificador, password: inputPassword };
}

function busquedaUsuario(loginResult, listaClientes) {
    // recorrer la lista con clientes
    const { identificador, password } = loginResult;

    var usuario;
    for (const iterator of listaClientes) {
        if (iterator.rut === identificador && iterator.clave === password) {
            usuario = iterator; //cliente existe
            break;
        }
    }
    return usuario;  
}

function validacionUsuario(usuario) {
    if (usuario) {
        alert("Bienvenido " + usuario.nombre)
    }else {
        alert("Datos incorrectos")
        throw new Error("Datos incorrectos")
    }
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
                verSaldo(usuario)
                break;

            case "2": //realizar giro
                giro(usuario)
                break;

            case "3": //realizar deposito
                depositar(usuario)
                break;

            case "4": //salir
                salir(usuario)
                break;
            default: //caso que se muestra por default si no cumple ningún caso
                alert("Opción incorrecta")
                break;
        }
    } while (opcion != "4");
}

function verSaldo(usuario) {
    alert("Su saldo es: " + usuario.saldo)

}

function giro(usuario){
    var retiro = parseInt(prompt("Su saldo actual es: "+ usuario.saldo + " Ingrese el monto que desea girar:"))
                if (retiro > usuario.saldo) {
                    alert("Saldo insuficiente")
                } else {
                    usuario.saldo -= retiro // acumulación de la resta del retiro al saldo del usuario
                    alert("Retiro completado, su nuevo saldo es: " + usuario.saldo)
                }
}

function depositar(usuario) {
    var deposito = parseInt(prompt("Su saldo actual es: "+ usuario.saldo + " Ingrese el monto que desea depositar:"))
                usuario.saldo += deposito
}

function salir(usuario) {
    alert("Hasta luego! " + usuario.nombre)
    
}

