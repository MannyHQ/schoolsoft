import { Router } from "express";

import { pagPayment, registerPays, pagProfile } from '../controllers/index-controllers.js';

const routes = Router();

routes.get( '/', (req, res) => res.redirect('/pagos'));
routes.get('/pagos', pagPayment);
routes.get('/historial', registerPays);
routes.get('/profile', pagProfile);

export default routes;