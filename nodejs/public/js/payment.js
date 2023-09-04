import MaskDate from "./components/mask_date.js";

const maskDate = new MaskDate();

function showPaymentForm(element, period) {
    
    const periodOptions = document.getElementsByClassName('period-option');
    for (let i = 0; i < periodOptions.length; i++)
        periodOptions[i].classList.remove('selected');
  
    element.classList.add('selected');

    document.getElementById('payment-form').style.display = 'block';
    document.getElementById('payment-period').style.display = 'none';
}

async function redirectToPayPal() {

    window.location.href = `/create-order`;
}
  
function showCardPaymentForm() {
    
    document.getElementById('card-details').style.display = 'block';
}

function showPaypalPaymentForm() {

    document.getElementBydId('paypal-details').style.display = 'block'
}

function showSuccessMessage() {
    
    const cardNumberInput = document.getElementById('card-number');
    const expiryInput = document.getElementById('expiry');
    const cvvInput = document.getElementById('cvv');
  
    if (cardNumberInput.value === '' || expiryInput.value === '' || cvvInput.value === '') {
        
        alert('Por favor, completa todos los campos');
    }

}

function cancelOptionPlan() {

    document.getElementById('payment-form').style.display = 'none';
    document.getElementById('payment-period').style.display = 'block';
    document.getElementById('card-details').style.display = 'none';
}
document.querySelector('.cancel-option').onclick = () => cancelOptionPlan();

document.querySelectorAll('.period-option').forEach(opt => {

    opt.onclick = () => showPaymentForm(opt, opt.textContent);
})

document.getElementById('paypal-option').onclick = () => redirectToPayPal();

document.getElementById('card-option').onclick = () => showCardPaymentForm();

