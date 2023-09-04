import mysql from 'mysql2';

import { DATABASE } from '../config.js';

export const getProfile = async (req, res) => {

    const user = req.session.usuario;
    
    const connection = await mysql.createConnection(DATABASE);

    const consulta = `SELECT * FROM Padres WHERE id_padre=${user.id_usuario}`;

    connection.query(consulta, (err, results, query) => {

        if ( err ) {

            console.log(err);
            res.json('no encontrado');
        }
        else{

            res.json(results[0]);
        }
    })

    connection.end();
}