document.addEventListener('DOMContentLoaded', function () {
    const caja1 = document.getElementById('caja1');
    const caja2 = document.getElementById('caja2');
    const boton1 = document.getElementById('boton1');
    const boton2 = document.getElementById('boton2');
    const contenido = document.getElementById('contenido');
    const texto = document.getElementById('texto');

    // Event listeners
    caja1.addEventListener('mouseover', mostrarMensaje);
    caja1.addEventListener('mouseout', ocultarMensaje);
    boton1.addEventListener('click', cambiarFondo);
    boton2.addEventListener('click', cambiarTexto);
    boton1.addEventListener('dblclick', volver);

    // Event handler functions
    function mostrarMensaje() {
        caja2.style.display = 'block';
    }

    function ocultarMensaje() {
        caja2.style.display = 'none';
    }

    function cambiarFondo() {
        contenido.style.backgroundColor = 'blue';
    }

    function cambiarTexto() {
        texto.innerHTML = 'Este es el nuevo texto';
    }

    function volver() {
        contenido.style.backgroundColor = 'coral';
    }
});
