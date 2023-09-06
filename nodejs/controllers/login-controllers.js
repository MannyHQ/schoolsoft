import path from 'path';
import mysql from 'mysql2';

import { DATABASE } from '../config.js';

export const pagLogin = (req, res) => res.sendFile(path.resolve('nodejs/public/html/login.html'));

export const userVerfication = async (req, res) => {

    const connection = await mysql.createConnection(DATABASE);

    connection.connect((err) => {

        if(err)
            console.log('\n<--- hubo un error --->\n', err);
        else
            console.log('conexion exitosa');
    })

    const consulta_login = `SELECT * FROM Usuario WHERE nombre_user='${req.body.username}' and password='${req.body.password}'`;

    connection.query(consulta_login, (err, results, fields) => {

        if (err)
            res.send('error al conectar')
        else{

            if (results.length > 0){
                
                req.session.usuario = results[0];
                res.send('true');
            }
            else
                res.send('false');
        }
    })

    connection.end();
}

export const checkLogin = (req, res) => {

    const check = req.session.usuario;

    if ( check ){

        res.send('true');
    }
    else 
        res.send('false')
}



export const removeSession = (req, res) => {

    req.session.destroy(err => {

        if  ( err ){

            res.send('hubo un error al borrar la session');
        }
        else    
            res.redirect('/index');
    })
}