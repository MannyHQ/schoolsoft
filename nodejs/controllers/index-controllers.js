import path from 'path';

export const pagPayment = (req, res) => res.sendFile(path.resolve('nodejs/public/html/metodo.html'));

export const registerPays = (req, res) => res.sendFile(path.resolve('nodejs/public/html/registroDePagos.html'));

export const pagProfile = (req, res) => res.sendFile(path.resolve('nodejs/public/html/profile.html'))