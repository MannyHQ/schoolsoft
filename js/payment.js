function showPaymentForm(element, period) {
    
    const periodOptions = document.getElementsByClassName('period-option');
    for (let i = 0; i < periodOptions.length; i++) {
        periodOptions[i].classList.remove('selected');
    }
  
    element.classList.add('selected');

    document.getElementById('payment-form').style.display = 'block';
    document.getElementById('payment-period').style.display = 'none';
    //document.getElementById('selected-period').innerText = 'Período seleccionado: ' + period;
}

function redirectToPayPal() {
    
    window.location.href = 'https://www.paypal.com';
}
  
function showCardPaymentForm() {
    
    document.getElementById('card-details').style.display = 'block';
}
  
function showSuccessMessage() {
    
    const cardNumberInput = document.getElementById('card-number');
    const expiryInput = document.getElementById('expiry');
    const cvvInput = document.getElementById('cvv');
  
    if (cardNumberInput.value === '' || expiryInput.value === '' || cvvInput.value === '') {
        
        alert('Por favor, completa todos los campos');
    }
  
    // const cardNumberFormatted = cardNumberInput.value.replace(/.(?=.{4})/g, '-');
    // cardNumberInput.value = cardNumberFormatted;
  
    // document.getElementById('payment-form').style.display = 'none';
    // document.getElementById('success-message').style.display = 'block';
}

function cancelOptionPlan() {

    document.getElementById('payment-form').style.display = 'none';
    document.getElementById('payment-period').style.display = 'block';
    document.getElementById('card-details').style.display = 'none';
}
document.querySelector('.cancel-option').onclick = () => cancelOptionPlan();