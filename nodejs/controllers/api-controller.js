import mysql, { createConnection } from 'mysql2';

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

export const setMatricula = async (req, res) => {

    const id = req.body.id_number;

    const connection = await mysql.createConnection(DATABASE);

    connection.connect(err => {

        if ( err ){

            res.send(` <-- hubo un error al conectar --> \n\n\n${err}`);
        }
    });

    const consultaIdStudent = `SELECT * FROM school_students where id_number=${id}`;

    connection.query(consultaIdStudent, (err, results, query) => {

        if ( err )
            res.send('usuario no encontrado')
        else{

            if ( results.length > 0) {

                req.session.matricula = id;
                res.send('true');
            }
            else
                res.send('false');
        }
    })
}

export const getPays = (req, res) => {

    const id = req.session.usuario.id_usuario;

    const connection = createConnection(DATABASE);

    const consulta_pays = `SELECT * FROM Pagos WHERE id_padre=${id}`;

    connection.query(consulta_pays, (err, results) => {

        if ( err ) {

            res.json('error en la consulta');
        }
        else {

            res.json(results);
        }
    })
}