const btnValidation = document.getElementById('btnValidation');

btnValidation.onclick = (e) => {
    e.preventDefault();

    const inpUsername = document.getElementById('username').value;
    const inpPassword = document.getElementById('password').value;

    fetch(`/verification/login/`, 
        { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username: inpUsername, password: inpPassword})
        }
    )
        .then(response => response.text())
        .then(text => {
            
            console.log(text);

            if (text === 'true'){
                
                window.location = `/profile`;
            }
            else
                alert('usuario no encontrado');
        })
        .catch((err) => {

            alert('error de inicio');
        });
}