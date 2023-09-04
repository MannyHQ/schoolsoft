import { Router } from "express";

import { pagLogin,userVerfication, checkLogin, removeSession } from '../controllers/login-controllers.js';

const routes = Router();

routes.get('/login', pagLogin);
routes.post('/verification/login/', userVerfication);
routes.get('/check-login', checkLogin);
routes.get('/logout', removeSession);

export default routes;