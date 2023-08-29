import express from 'express';
import bodyParse from 'body-parser';
import session from 'express-session';
import path from 'path';

import indexPages from './routes/index.routes.js';
import loginPages from './routes/login.routes.js';
import paymentPages from './routes/payments.routes.js';

import { PORT } from './config.js';

const app = express();

app.use(bodyParse.urlencoded({ extended: true }));
app.use(express.static(path.resolve('nodejs/public')));
app.use(session({ secret: 'your-secret-key', resave: true, saveUninitialized: true }));
app.use(express.text());
app.use(express.json());

app.use(indexPages);
app.use(loginPages);
app.use(paymentPages);

app.listen(PORT, () => {

    console.log('el servidor esta escuchando');
})