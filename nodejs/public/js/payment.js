import MaskDate from "./components/mask_date.js";
import MaskMatricula from "./components/mask_matricula.js";



// import MaskCVV from "./components/mask_cvv.js";

// const maskCvv = new MaskCVV();
// const maskDate = new MaskDate();


const maskMatricula = new MaskMatricula();

let mont = 0;

let mensualidad; // Variable donde almacenarás la mensualidad

// Realiza una solicitud HTTP para obtener la mensualidad
fetch('/mensualidad')
  .then((response) => response.json())
  .then((data) => {
    mensualidad = data.mensualidad; // Almacena la mensualidad en la variable
    console.log('El valor de la mensualidad es:', mensualidad);

    // Puedes usar la variable 'mensualidad' en este archivo JavaScript como desees
    // Por ejemplo, puedes realizar acciones adicionales con la mensualidad o mostrarla en la consola
  })
  .catch((error) => {
    console.error('Error al obtener la mensualidad:', error);
  });


function showPaymentForm(element, period) {

    let text = element.textContent.trim();
    
    if ( text === '1 Mes' )
        mont = mensualidad*1;
    else if ( text === '1 Año')
        mont = mensualidad*12;

    const periodOptions = document.getElementsByClassName('period-option');
    for (let i = 0; i < periodOptions.length; i++)
        periodOptions[i].classList.remove('selected');
  
    element.classList.add('selected');

    document.getElementById('payment-form').style.display = 'block';
    document.getElementById('payment-period').style.display = 'none';
}

function redirectToPayPal() {

    const id = document.getElementById('idStudent').value;
    console.log(id);

    fetch('/api/set/matricula', 
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({id_number: id})
        }
    )
    .then(response => response.text())
    .then(text => {

        if ( text === 'true' ) {

            window.location.href = `/create-order?mont=${mont}`;
        }
        else {

            console.log(text);
            alert('estudiante no encontrado');
        }
    })
    .catch(err => {

        console.log(err);
    })
}
  
// function showCardPaymentForm() {
    
//     document.getElementById('card-details').style.display = 'block';
//     document.getElementById('paypal-details').style.display = 'none';
// }

function showPaypalPaymentForm() {

    document.getElementById('paypal-details').style.display = 'block';
    // document.getElementById('card-details').style.display = 'none';
}

// function showSuccessMessage() {
    
//     const cardNumberInput = document.getElementById('card-number');
//     const expiryInput = document.getElementById('expiry');
//     const cvvInput = document.getElementById('cvv');
  
//     if (cardNumberInput.value === '' || expiryInput.value === '' || cvvInput.value === '') {
        
//         alert('Por favor, completa todos los campos');
//     }

// }

function cancelOptionPlan() {

    document.getElementById('payment-form').style.display = 'none';
    document.getElementById('payment-period').style.display = 'block';
    // document.getElementById('card-details').style.display = 'none';
    document.getElementById('paypal-details').style.display = 'none';
}
document.querySelector('.cancel-option').onclick = () => cancelOptionPlan();

document.querySelectorAll('.period-option').forEach(opt => {

    opt.onclick = () => showPaymentForm(opt, opt.textContent);
})

document.getElementById('paypal-option').onclick = () => showPaypalPaymentForm();

// document.getElementById('card-option').onclick = () => showCardPaymentForm();

document.getElementById('btnSubmitPaypal').onclick = () => redirectToPayPal();