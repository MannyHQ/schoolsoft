const registerContain = document.querySelector('.field-container');

const html = [];
const dataPays = [];
const dataFather = [];

const request = async (url) => {

    const response = await fetch(url);
    const data = await response.json();

    return data;
} 

const pays = request('/api/get/pays');
const father = request('/api/profile');

await pays.then(json => {

        json.forEach( data => {

            dataPays.push(data);
        })
    });

await father.then(json => {

        dataFather.push(json);
    });

    // titulos de los campos
html.push(`<div class="field-titles">
    <div class="field-element">id pago</div>
    <div class="field-element">id estudiante</div>
    <div class="field-element">fecha de pago</div>
    <div class="field-element">monto</div>
    <div class="field-element">id padre</div>
    <div class="field-element">telefono</div>
    <div class="field-element">cedula</div>
</div>`);

dataPays.forEach( data => {

    const field = `<div class="field-data">
        <div class="field-element">${data.id_pago}</div>
        <div class="field-element">${data.id_estudiante}</div>
        <div class="field-element">${data.fecha_pago.substring(0, 10)}</div>
        <div class="field-element">${data.monto_total}</div>
        <div class="field-element">${dataFather[0].id_padre}</div>
        <div class="field-element">${dataFather[0].telefono}</div>
        <div class="field-element">${dataFather[0].cedula}</div>
    </div>`;

    html.push(field);
})

registerContain.innerHTML += html.join('');