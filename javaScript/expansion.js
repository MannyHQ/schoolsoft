const centro_Options = document.querySelector('#Centro-Options')
const expansivo1 = document.querySelector('.cuadro1');
const originalHTML = expansivo1.innerHTML;


const expansivo2 = document.querySelector('.cuadro2');
const expansivo3 = document.querySelector('.cuadro3');
const expansivo4 = document.querySelector('.cuadro4');
const expansivo5 = document.querySelector('.cuadro5');
const expansivo6 = document.querySelector('.cuadro6');
const expansivo7 = document.querySelector('.cuadro7');
const expansivo8 = document.querySelector('.cuadro8');
let expandido = false;
expansivo2.a = 'muestra';
expansivo3.a = 'muestra';
expansivo4.a = 'muestra';
expansivo5.a = 'muestra';
expansivo6.a = 'muestra';
expansivo7.a = 'muestra';
expansivo8.a = 'muestra';

expansivo1.addEventListener('click', ()=>{
    let data;
    if(!expandido){
        centro_Options.style = `grid-template-areas: 
        "one one one"
        "one one one"
        "one one one"
        "two two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        data = expansivo1;
        data.id = 'content';
        data.style = `background-color: #6AA5A9;`
        data.innerHTML = `<h1>Calificaciones Destacadas </h1>
        <table class="table">
            <thead>
                <tr class="">
                <th scope="col">Curso</th>
                <th scope="col">Nombre</th>
                <th scope="col">Materia</th>
                <th scope="col">Calificacion</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>95.5</td>
                </tr>
                <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>89.3</td>
                </tr>
                <tr>
                <th scope="row">3</th>
                <td>Larry</td>
                <td>the Bird</td>
                <td>91</td>
                </tr>
                <tr>
                <th scope="row">4</th>
                <td>Dani</td>
                <td>the Bird</td>
                <td>98</td>
                </tr>
            </tbody>
        </table>`
        expandido = true;
    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        data = expansivo1;
        data.style = `background-color: none;`
        data.innerHTML = originalHTML;
        expandido = false;
    }
})
expansivo2.addEventListener('click', ()=>{
    if(expansivo2.a === 'muestra' ){
        centro_Options.style = `grid-template-areas: 
        "two two two"
        "two two two"
        "two two two"
        "one one nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo2.style = 'background-color: #AEAEAE;';
        expansivo2.a = 'nuevo contenido'

    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo2.a = 'muestra'
    }
})
expansivo3.addEventListener('click', ()=>{
    if(expansivo3.a === 'muestra' ){
        centro_Options.style = `grid-template-areas: 
        "thre thre thre"
        "thre thre thre"
        "thre thre thre"
        "one one nine"
        "two four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo3.style = 'background-color: #AEAEAE;';
        expansivo3.a = 'nuevo contenido'

    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo3.a = 'muestra'
    }
})
expansivo4.addEventListener('click', ()=>{
    if(expansivo4.a === 'muestra'){
        centro_Options.style = `grid-template-areas: 
        "four four four"
        "four four four"
        "four four four"
        "one two nine"
        "thre thre nine"
        "five six nine"
        "seven heigh ten";`
        expansivo4.style = 'background-color: #AEAEAE;';
        expansivo4.a = 'nuevo contenido'

    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo4.a = 'muestra'
    }
})
expansivo5.addEventListener('click', ()=>{
    if(expansivo5.a === 'muestra' ){
        centro_Options.style = `grid-template-areas: 
        "five five five"
        "five five five"
        "five five five"
        "one two nine"
        "thre four nine"
        "six six nine"
        "seven heigh ten";`
        expansivo5.style = 'background-color: #AEAEAE;';
        expansivo5.a = 'nuevo contenido'

    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo5.a = 'muestra'
    }
})
expansivo6.addEventListener('click', ()=>{
    if(expansivo6.a === 'muestra' ){
        centro_Options.style = `grid-template-areas: 
        "six six six"
        "six six six"
        "six six six"
        "one two nine"
        "thre four nine"
        "five five nine"
        "seven heigh ten";`
        expansivo6.style = 'background-color: #AEAEAE;';
        expansivo6.a = 'nuevo contenido'

    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo6.a = 'muestra'
    }
})
expansivo7.addEventListener('click', ()=>{
    if(expansivo7.a === 'muestra' ){
        centro_Options.style = `grid-template-areas: 
        "seven seven seven"
        "seven seven seven"
        "seven seven seven"
        "one two nine"
        "thre four nine"
        "five six nine"
        "heigh heigh ten";`
        expansivo7.style = 'background-color: #AEAEAE;';
        expansivo7.a = 'nuevo contenido'

    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo1.a = 'muestra'
    }
})
expansivo8.addEventListener('click', ()=>{
    if(expansivo8.a === 'muestra' ){
        centro_Options.style = `grid-template-areas: 
        "heigh heigh heigh"
        "heigh heigh heigh"
        "heigh heigh heigh"
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven seven ten";`
        expansivo8.style = 'background-color: #AEAEAE;';
        expansivo8.a = 'nuevo contenido'

    }else{
        centro_Options.style = `grid-template-areas: 
        "one two nine"
        "thre four nine"
        "five six nine"
        "seven heigh ten";`
        expansivo8.a = 'muestra'
    }
})