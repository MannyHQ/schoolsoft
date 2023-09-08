import axios from "axios";
import mysql from 'mysql2';
import path from 'path';

import { PAYPAL_API, PAYPAL_API_CLIENT, PAYPAL_API_SECRET, HOST, DATABASE } from "../config.js";

export const createOrder = async (req, res) => {

    const params = new URLSearchParams();
    params.append('grant_type', 'client_credentials');

    const { data: {access_token} } = await axios.post(`${PAYPAL_API}/v1/oauth2/token/`, params,
        {
            auth: {
                username : PAYPAL_API_CLIENT,
                password : PAYPAL_API_SECRET
            }
        }
    );

    const order = {
        intent: 'CAPTURE',
        purchase_units: [
            {
                amount: {
                    currency_code: 'USD',
                    value: req.query.mont
                }
            }
        ],
        application_context: {
            brand_name: 'schoolsoft',
            landing_page: 'NO_PREFERENCE',
            user_action: 'PAY_NOW',
            return_url: `${HOST}/capture-order`,
            cancel_url: `${HOST}/cancel-order`
        }
    };

    req.session.amount = order.purchase_units[0].amount.value;

    const response = await axios.post(`${PAYPAL_API}/v2/checkout/orders`, order, 
        {
            headers: {
                Authorization: `Bearer ${access_token}`
            }
        }
    );

    res.redirect(response.data.links[1].href);
}

function processId(id) {

    let newId = ''

    for ( let char of id ) {

        if ( !isNaN(parseInt(char)) ) {

            newId += char; 
        }

        if ( newId.length === 8)
            break;
    }

    return newId;
}

export const captureOrder = async (req, res) => {

    const { token } = req.query;

    const response = await axios.post(`${PAYPAL_API}/v2/checkout/orders/${token}/capture`, {},
        {
            auth : {
                username : PAYPAL_API_CLIENT,
                password : PAYPAL_API_SECRET
            }
        }
    )

    const connection = mysql.createConnection(DATABASE);
    
    const id_pay = processId(response.data.id);
    const id_father = req.session.usuario.id_usuario;

    const consulta_pay = `INSERT INTO school_billing (id_pago, id_padre_id, id_estudiante_id, fecha_pago, monto_total, estado)
        values (?, ?, ?, ?, ?, ?)`;
    const values_pay = [parseInt(id_pay), id_father, req.session.matricula, new Date().toISOString().split('T')[0], req.session.amount, 1];

    connection.query(consulta_pay, values_pay, (err, results, fields) => {

        if ( err ) {

            res.send(err);
        }
        else {

            req.session.amount = null;
            res.sendFile(path.resolve('nodejs/public/html/pagoRealizado.html'));
        }
    });
};

export const cancelOrder = (req, res) => res.sendFile(path.resolve('nodejs/public/html/pagoCancelado.html'));