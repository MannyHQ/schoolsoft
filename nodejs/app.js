import express from 'express';
import bodyParse from 'body-parser';
import session from 'express-session';
import path from 'path';

import indexPages from './routes/index.routes.js';
import loginPages from './routes/login.routes.js';
import paymentPages from './routes/payments.routes.js';
import apiResources from './routes/api.routes.js';

import { PORT } from './config.js';

import consulta from './controllers/mensualidad.js'

const app = express();

// modulos
app.use(bodyParse.urlencoded({ extended: true }));
app.use(express.static(path.resolve('nodejs/public')));
app.use(session(
    { 
        secret: 'user', 
        resave: true, 
        saveUninitialized: true,
        cookie: { secure: false }
    }
));
app.use(express.text());
app.use(express.json());

// recursos publicos
app.use(indexPages);
app.use(loginPages);
app.use(paymentPages);
app.use(apiResources);

 app.get('/mensualidad', (req, res) => {
     // Utiliza la función obtenerMensualidad de consulta.js para obtener la mensualidad desde la base de datos
     consulta.obtenerMensualidad((err, mensualidad) => {
       if (err) {
         console.error('Error al obtener la mensualidad:', err);
         return;
       }
    
       // Envía la mensualidad como respuesta JSON al cliente
       res.send({ mensualidad });
     });
   });


app.listen(PORT, () => {

    console.log(`el servidor esta escuchando en el puerto ${PORT}`);
})