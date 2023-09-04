import { Router } from "express";

import { getProfile } from "../controllers/api-controller.js";

const routes = Router();

routes.get('/api/profile', getProfile);

export default routes;