import { Router } from "express";

import { createOrder, captureOrder, cancelOrder } from '../controllers/payments_controllers.js';

const routes = Router();

routes.get('/create-order', createOrder);
routes.get('/capture-order', captureOrder);
routes.get('/cancel-order', cancelOrder);

export default routes;