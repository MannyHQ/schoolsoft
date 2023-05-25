const div= document.querySelectorAll(".opciones_de_clase")
const opcion=document.querySelectorAll(".datos_de_clase")

/*for(const divs of div){
    divs.addEventListener('click',()=>{
        for(const opciones of opcion){ 
               opciones.setAttribute('style','display:block')
        }
    })
}*/

div.forEach((elemento,clave)=>{
    elemento.addEventListener('click',()=>{
        opcion[clave].classList.toggle("visible")
    })
})