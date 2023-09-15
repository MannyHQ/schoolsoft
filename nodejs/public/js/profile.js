fetch('/api/profile')
    .then(response => { return response.json() })
    .then(json => {

        const elementsValue = document.querySelectorAll('.element-value');
        
        elementsValue[0].textContent = json.first_name;
        elementsValue[1].textContent = json.last_name;
        elementsValue[2].textContent = json.mail;
        elementsValue[3].textContent = json.phone_number;
        elementsValue[4].textContent = json.id_number;
    });