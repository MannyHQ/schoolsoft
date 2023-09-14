import { Router } from "express";

import { getPays, getPdf, getProfile, setMatricula } from "../controllers/api-controller.js";

const routes = Router();

routes.get('/api/profile', getProfile);
routes.post('/api/set/matricula', setMatricula);
routes.get('/api/get/pays', getPays);
routes.get( '/api/get/pays/pdf', getPdf);

export default routes;