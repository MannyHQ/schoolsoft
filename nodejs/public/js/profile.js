fetch('/api/profile')
    .then(response => { return response.json() })
    .then(json => {

        const elementsValue = document.querySelectorAll('.element-value');

        elementsValue[0].textContent = json.nombre;
        elementsValue[1].textContent = json.apellido;
        elementsValue[2].textContent = json.correo;
        elementsValue[3].textContent = json.telefono;
        elementsValue[4].textContent = json.cedula;
    });