import path from 'path';

export const pagPrincipal = (req, res) => res.sendFile(path.resolve('nodejs/public/html/eventos.html'));

export const pagPayment = (req, res) => res.sendFile(path.resolve('nodejs/public/html/metodo.html'));

export const registerPays = (req, res) => res.sendFile(path.resolve('nodejs/public/html/registroDePagos.html'));