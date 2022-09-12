const $formularioRegistro = document.getElementById('formularioRegistro');
const $txtNombre = document.getElementById('txtNombre');
const $txtCiudad = document.getElementById('txtCiudad');

(function () {

    $formularioRegistro.addEventListener('submit', function (e) {
        let nombre = String($txtNombre.value).trim();
        if (nombre.length === 0) {
            alert("El nombre no puede ir vacío...");
            e.preventDefault();
        }
    });

})();


(function () {

    $formularioRegistro.addEventListener('submit', function (e) {
        let ciudad = String($txtCiudad.value).trim();
        if (ciudad.length === 0) {
            alert("La ciudad no puede ir vacía...");
            e.preventDefault();
        }
    });

})();