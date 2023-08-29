const btnValidation = document.getElementById('btnValidation');

btnValidation.onclick = () => {

    const inpUsername = document.getElementById('username').value;
    const inpPassword = document.getElementById('password').value;

    fetch(`http://localhost:3000/verification/login/${inpUsername}-${inpPassword}`)
        .then(response => response.json())
        .then(json => {
            
            if (json.length > 0)
                window.location = 'http://localhost:3000/index';
        });
}