const btnProfile = document.getElementById('father-profile');

fetch('/check-login')
    .then(response => response.text())
    .then((text) => {

        if ( text === 'true' ) {
        
            // mostrando boton del pefil
            btnProfile.style.display = 'block';

            // eleminando los botones de iniciar una cuenta por defecto
            document.getElementById('father-login').style.display = 'none';
        }
    })
    .catch((err) => {

        console.log(err);
    });