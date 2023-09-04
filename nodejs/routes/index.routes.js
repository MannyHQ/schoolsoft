import { Router } from "express";

import { pagPrincipal, pagPayment, registerPays, pagProfile } from '../controllers/index-controllers.js';

const routes = Router();

routes.get('/index', pagPrincipal);
routes.get('/pagos', pagPayment);
routes.get('/historial', registerPays);
routes.get('/profile', pagProfile);

export default routes;