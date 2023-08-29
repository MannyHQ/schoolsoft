import { Router } from "express";

import { pagLogin, userVerfication } from '../controllers/login-controllers.js';

const routes = Router();

routes.get('/login', pagLogin);
routes.get('/verification/login/:user', userVerfication);

export default routes;