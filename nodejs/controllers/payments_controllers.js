import axios from "axios";

import { PAYPAL_API, PAYPAL_API_CLIENT, PAYPAL_API_SECRET, HOST } from "../config.js";

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
                    value: '100.00'
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

    const response = await axios.post(`${PAYPAL_API}/v2/checkout/orders`, order, 
        {
            headers: {
                Authorization: `Bearer ${access_token}`
            }
        }
    );

    res.redirect(response.data.links[1].href);
}

export const captureOrder = async (req, res) => {

    const { token } = req.params;

    const response = await axios.post(`${PAYPAL_API}/v2/checkout/orders/${token}/capture`, {},
        {
            auth : {
                username : PAYPAL_API_CLIENT,
                password : PAYPAL_API_SECRET
            }
        }
    )

    console.log(response.data);

    res.json('payed');
};

export const cancelOrder = (req, res) => res.send('cancelOrder');