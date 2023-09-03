const div= document.querySelectorAll(".mateasig")
const opcion=document.querySelectorAll(".notas_invisibles")
div.forEach((elemento,clave)=>{
    elemento.addEventListener('click',()=>{
        opcion[clave].classList.toggle("notas_visibles")
    })
})