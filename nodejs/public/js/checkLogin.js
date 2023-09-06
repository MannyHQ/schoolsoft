const btnProfile = document.getElementById('father-profile');

const link = window.location.pathname;

fetch('/check-login')
    .then(response => response.text())
    .then((text) => {


        if ( text === 'true' ) {
        
            // mostrando boton del pefil
            btnProfile.style.display = 'block';

            // eleminando los botones de iniciar una cuenta por defecto
            document.getElementById('father-login').style.display = 'none';
        }
        else if ( link === '/pagos' || link === '/historial') {

            alert('no has iniciado session');
            window.location.href = '/index';
        }
    })
    .catch((err) => {

        console.log(err);
    });