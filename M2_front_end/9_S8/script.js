// ciclos en javascript, ciclo for, while, do while

// ciclo for
// for (let index = 0; index < array.length; index++) {
//     const element = array[index];
// }

for (let i = 0; i < 5; i++) {
    console.log(i);
}

// ciclo while, solo se ejecuta si la condición se cumple
// while (condition) {
    
// }

let i = 0;
while (i < 5) {
    console.log(i);
    i++; // i += 1
}

// do while, se ejecuta al menos una vez
i = 0;
do {
    console.log(i);
    i++; // aumentar el valor del iterador para salir del ciclo
} while (i < 5);


////////////////////////////////////////////////////////////////////////////////////////////////////////
let colores = ["verde", "rojo", "azul"] // [0,1,2] -> arreglo que contiene 3 elmentos
                                        // ["verde", "rojo", "azul"]
//con ciclo for
for (let i = 0; i < colores.length; i++) {
    console.log(colores[i]);
    
}

//con ciclo while
i = 0;
while (i < colores.length) {
    console.log(colores[i]);
    i++;
}

//con ciclo do while

i = 0;
do {
    console.log(colores[i]);
    i++;
} while (i < colores.length);

