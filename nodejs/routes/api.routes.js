import { Router } from "express";

import { getPays, getProfile, setMatricula } from "../controllers/api-controller.js";

const routes = Router();

routes.get('/api/profile', getProfile);
routes.post('/api/set/matricula', setMatricula);
routes.get('/api/get/pays', getPays);

export default routes;