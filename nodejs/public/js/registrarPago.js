const registerContain = document.querySelector('.field-container');

fetch('/api/get/pays')
    .then(response => response.json())
    .then(json => {

        const html = [];

        // titulos de los campos
        html.push(`<div class="field-titles">
        <div class="field-element">id pago</div>
        <div class="field-element">id estudiante</div>
        <div class="field-element">fecha de pago</div>
        <div class="field-element">monto</div>
    </div>`)

        // 
        json.forEach( register => {

            html.push(`
            <div class="field-data">
                <div class="field-element">${register.id_pago}</div>
                <div class="field-element">${register.id_estudiante}</div>
                <div class="field-element">${register.fecha_pago.substring(0, 10)}</div>
                <div class="field-element">${register.monto_total}</div>
            </div>    
            `)
        })

        registerContain.innerHTML = html.join('');
    })