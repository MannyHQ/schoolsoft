const nota = document.getElementById("container");
const centro_Options = document.querySelector('#Centro-Options');
const expansivo1 = document.querySelector('.cuadro1');
const expansivo2 = document.querySelector('.cuadro3');
const expansivo5 = document.querySelector('.cuadro5');
const expansivo7 = document.querySelector('.cuadro7');

const originalHTML = expansivo1.innerHTML;
const valor = expansivo2.innerHTML;
const originExpansivo5 = expansivo5.innerHTML;
const originExpansivo7 = expansivo7.innerHTML;

let expandido1 = false;
let expandido2 = false;
let expandido5 = false;
let expandido7 = false;

expansivo1.addEventListener('click', ()=>{
    let data;
    if(!expandido1){
        centro_Options.style = `grid-template-areas: 
        "one one one"
        "one one one"
        "one one one"
        "two thre nine"
        "four five nine"
        "seven seven nine";`
        data = expansivo1;
        data.class = 'cuadrado1';
        data.style = `background-color: #6AA5A9;`
        data.innerHTML = `<h1>Calificaciones Destacadas </h1>
        <table class="table">
            <tr>
                <th>Curso</th>
                <th>Num Lista</th>
                <th>Nombre</th>
                <th>Apellido</th>
                <th>Materia</th>
                <th>Clasificacion</th>
            </tr>
            <tr>
                <td>1A</td>
                <td>2</td>
                <td>Jose</td>
                <td>Adrian</td>
                <td>Ingles</td>
                <td>96</td>
            </tr>
            <tr>
                <td>1B</td>
                <td>8</td>
                <td>Antoni</td>
                <td>Rodriguez</td>
                <td>C. Sociales</td>
                <td>99</td>
            </tr>
            <tr>
                <td>1A</td>
                <td>13</td>
                <td>Pedro</td>
                <td>Guzman</td>
                <td>Frances</td>
                <td>94</td>
            </tr>
            <tr>
                <td>1A</td>
                <td>2</td>
                <td>Jose</td>
                <td>Adrian</td>
                <td>Ingles</td>
                <td>96</td>
            </tr>
            <tr>
                <td>1B</td>
                <td>8</td>
                <td>Antoni</td>
                <td>Rodriguez</td>
                <td>C. Sociales</td>
                <td>99</td>
            </tr>
            <tr>
                <td>1A</td>
                <td>13</td>
                <td>Pedro</td>
                <td>Guzman</td>
                <td>Frances</td>
                <td>94</td>
            </tr>
            <tr>
                <td>1A</td>
                <td>2</td>
                <td>Jose</td>
                <td>Adrian</td>
                <td>Ingles</td>
                <td>96</td>
            </tr>
            <tr>
                <td>1B</td>
                <td>8</td>
                <td>Antoni</td>
                <td>Rodriguez</td>
                <td>C. Sociales</td>
                <td>99</td>
            </tr>
            <tr>
                <td>1A</td>
                <td>13</td>
                <td>Pedro</td>
                <td>Guzman</td>
                <td>Frances</td>
                <td>94</td>
            </tr>
        </table>`
        expandido1 = true;
    }else{
        centro_Options.style = `grid-template-areas: 
        "one one nine"
        "two thre nine"
        "four five nine"
        "seven seven nine";`
        data = expansivo1;
        data.style = `background-color: none;`
        data.innerHTML = originalHTML;
        expandido1 = false;
    }
});

expansivo2.addEventListener('click', ()=>{
    let data2;
    if(!expandido2){
        centro_Options.style = `grid-template-areas: 
        "thre thre thre"
        "thre thre thre"
        "thre thre thre"
        "one two nine"
        "four five nine"
        "seven seven nine"`
        data2 = expansivo2;
        data2.style = 'background-color: #6AA5A9;'
        data2.innerHTML = `
        <section id="chat">
            <div class="container py-5">
            <div class="row d-flex justify-content-center">
                <div class="col-md-8 col-lg-6 col-xl-4" id="chat">
                <div class="card">
                    <div class="card-header d-flex justify-content-between align-items-center p-3"
                    style="border-top: 4px solid #ffa900;">
                    <h5 class="mb-0">Chat messages</h5>
                    <div class="d-flex flex-row align-items-center">
                        
                        <span class="badge bg-warning me-3">20</span>
                        <i class="fas fa-minus me-3 text-muted fa-xs"></i>
                        <i class="fas fa-comments me-3 text-muted fa-xs"></i>
                        <a id="volver" class="btn btn-primary" href="/schoolsoft/index.html"><i class="fas fa-times text-muted fa-xs"></i></a>
                    </div>
                    </div>
                    <div class="card-body" data-mdb-perfect-scrollbar="true" style="position: relative; height: 400px">
        
                    <div class="d-flex justify-content-between">
                        <p class="small mb-1">Timona Siera</p>
                        <p class="small mb-1 text-muted">23 Jan 2:00 pm</p>
                    </div>
                    <div class="d-flex flex-row justify-content-start">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava5-bg.webp"
                        alt="avatar 1" style="width: 45px; height: 100%;">
                        <div>
                        <p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">For what reason
                            would it
                            be advisable for me to think about business content?</p>
                        </div>
                    </div>
        
                    <div class="d-flex justify-content-between">
                        <p class="small mb-1 text-muted">23 Jan 2:05 pm</p>
                        <p class="small mb-1">Johny Bullock</p>
                    </div>
                    <div class="d-flex flex-row justify-content-end mb-4 pt-1">
                        <div>
                        <p class="small p-2 me-3 mb-3 text-white rounded-3 bg-warning">Thank you for your believe in
                            our
                            supports</p>
                        </div>
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp"
                        alt="avatar 1" style="width: 45px; height: 100%;">
                    </div>
        
                    <div class="d-flex justify-content-between">
                        <p class="small mb-1">Timona Siera</p>
                        <p class="small mb-1 text-muted">23 Jan 5:37 pm</p>
                    </div>
                    <div class="d-flex flex-row justify-content-start">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava5-bg.webp"
                        alt="avatar 1" style="width: 45px; height: 100%;">
                        <div>
                        <p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">Lorem ipsum dolor
                            sit amet
                            consectetur adipisicing elit similique quae consequatur</p>
                        </div>
                    </div>
        
                    <div class="d-flex justify-content-between">
                        <p class="small mb-1 text-muted">23 Jan 6:10 pm</p>
                        <p class="small mb-1">Johny Bullock</p>
                    </div>
                    <div class="d-flex flex-row justify-content-end mb-4 pt-1">
                        <div>
                        <p class="small p-2 me-3 mb-3 text-white rounded-3 bg-warning">Dolorum quasi voluptates quas
                            amet in
                            repellendus perspiciatis fugiat</p>
                        </div>
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp"
                        alt="avatar 1" style="width: 45px; height: 100%;">
                    </div>
        
                    </div>
                    <div class="card-footer text-muted d-flex justify-content-start align-items-center p-3">
                    <div class="input-group mb-0">
                        <input type="text" class="form-control" placeholder="Type message"
                        aria-label="Recipient's username" aria-describedby="button-addon2" />
                        <button class="btn btn-warning" type="button" id="button-addon2" style="padding-top: .55rem;">
                        Button
                        </button>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </section>`;
        expandido2 = true;
    }
    // }else{
    //     centro_Options.style = `grid-template-areas: 
    //     "one one nine"
    //     "two thre nine"
    //     "four five nine"
    //     "seven seven nine";`;
    //     data2 = expansivo2;
    //     data2.innerHTML = valor;
    //     expandido2 = false;
    // }
})
expansivo5.addEventListener('click', ()=>{
    let data;
    if(!expandido5){
        centro_Options.style = `grid-template-areas: 
        "five five five"
        "five five five"
        "five five five"
        "one two nine"
        "thre four nine"
        "seven seven nine"`
        data = expansivo5;
        data.style = 'background-color: #6AA5A9;'
        data.innerHTML = `
        <div class="fijado">
            <nav id="cabeza" class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand">Trabajos Fijados</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <form class="d-flex">
                            <input id="search" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                        </form>
                    </div>
                    <a id="volver" class="btn btn-primary" href="/schoolsoft/index.html">volver</a>
                </div>
            </nav>
            <div class="container my-3" id="container">
                <div id="cont" class="card text-dark bg-light mb-3">
                    <div class="card-body">
                        <h5 class="card-title">Trabajo a Fijar</h5>
                        <div class="form-group">
                            <textarea id="addNote" class="form-control" aria-label="With textarea"></textarea>
                        </div>
                        <br />
                        <button id="addBtn" class="btn btn-primary">Add</button>
                    </div>
                </div>
                
                <hr>
                
                <div id="noMatches" class="row container-fluid">
                
                </div>
                
                <div id="notes" class="row container-fluid">
                
                </div>
            </div>
        </div>
        <script src="/schoolsoft/javaScript/script.js"></script>`
        expandido5 = true;

    }
    // else{
    //     centro_Options.style = `grid-template-areas: 
    //     "one one nine"
    //     "two thre nine"
    //     "four five nine"
    //     "seven seven nine";`;
    //     data = expansivo5;
    //     data.innerHTML = originExpansivo5;
    //     expandido5 = false;
    // }
})

expansivo7.addEventListener('click', ()=>{
    let data;
    if(!expandido7){
        centro_Options.style = `grid-template-areas: 
        "seven seven seven"
        "seven seven seven"
        "seven seven seven"
        "one two nine"
        "thre four nine"
        "five five nine"`
        data = expansivo7;
        data.style = 'background-color: #6AA5A9;'
        data.innerHTML = `
        <div class="fijado">
            <nav id="cabeza" class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand">Archivos</a>
                    <a id="volver" class="btn btn-primary" href="/schoolsoft/index.html">volver</a>
                </div>
            </nav>
            <div class="container mt-5">
                <h1>Carga de archivos</h1>
                <form action="upload.php" method="POST" enctype="multipart/form-data">
                <div class="mb-3">
                    <label for="fileInput" class="form-label">Archivar:</label>
                    <input type="file" class="form-control" id="fileInput" name="fileInput">
                </div>
                <button type="submit" class="btn btn-primary">Upload</button>
                </form>
            </div>
        </div>`;
        expandido7 = true;
    }

    // }else{
    //     centro_Options.style = `grid-template-areas: 
    //     "one one nine"
    //     "two thre nine"
    //     "four five nine"
    //     "seven seven nine";`;
    //     data = expansivo7;
    //     data.innerHTML = originExpansivo7;
    //     expandido7 = false;
    // }
})