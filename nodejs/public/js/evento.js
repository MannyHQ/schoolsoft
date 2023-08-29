// Supongamos que tienes un array de eventos llamado "eventosColegio"
const eventosColegio = [
    {
      titulo: "Título del evento 1",
      descripcion: "Descripción del evento 1",
      fecha: "Fecha del evento 1"
    },
    {
      titulo: "Título del evento 2",
      descripcion: "Descripción del evento 2",
      fecha: "mamaguebo"
    },
    // Agrega más eventos aquí
  ];
  
// Función para generar la lista de eventos
function generarListaEventos() {

    const eventList = document.querySelector('.event-list');
  
    // Vaciar la lista de eventos existente
    eventList.innerHTML = '';
  
    // Generar y agregar cada evento a la lista
    eventosColegio.forEach(evento => {
      
        const eventItem = document.createElement('li');
        eventItem.classList.add('event-item');
  
        const title = document.createElement('h3');
        title.classList.add('event-title');
        title.textContent = evento.titulo;
  
        const description = document.createElement('p');
        description.classList.add('event-description');
        description.textContent = evento.descripcion;

        const date = document.createElement('p');
        date.classList.add('event-date');
        date.textContent = evento.fecha;
  
        eventItem.appendChild(title, description, date);
  
        eventList.appendChild(eventItem);
    });
}
  
// Llamar a la función para generar la lista de eventos al cargar la página
generarListaEventos();
  