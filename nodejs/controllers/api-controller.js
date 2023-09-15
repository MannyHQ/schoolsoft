import mysql, { createConnection } from 'mysql2';
import mysql2 from 'mysql2/promise.js'
import fs from 'fs';
import { DATABASE } from '../config.js';

export const getProfile = async (req, res) => {

    const id = req.session.usuario.id_usuario;
    
    const connection = await mysql.createConnection(DATABASE);

    const consulta = `SELECT * FROM school_parents WHERE id=${id}`;

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

    connection.end()
}

export const getPays = async (req, res) => {

    const id = req.session.usuario.id_usuario;

    const connection = createConnection(DATABASE);

    const consulta_pays = `SELECT * FROM school_pagos WHERE id_padre=${id}`;

    connection.query(consulta_pays, (err, results) => {

        if ( err ) {

            res.json('error en la consulta');
        }
        else {

            res.json(results);
        }
    })

    connection.end();
}

import PDFDocument from 'pdfkit';

export const getPdf = async (req, res) => {

    // conectamos la base de datos para obtener la informacion para el pdf

    const id = req.session.usuario.id_usuario;
    console.log(req.session.usuario.id_usuario);
    const connection = await mysql2.createConnection(DATABASE);

    await connection.connect(err => {

        if ( err )
            return err;
    })

    const consulta_pays = `SELECT * FROM school_pagos WHERE id_padre=${id}`;
    const [pays] = await connection.execute(consulta_pays);
    const consulta_profile = `SELECT * FROM school_parents WHERE id=${id}`;
    const [profile] = await connection.execute(consulta_profile);

    connection.end();

    // toda la informacion se ordenara y guardara en este array de objetos
    const registerPays = [];

    pays.forEach( register => {

        registerPays.push(
            `
                id_pago: ${register.id_pago},
                id_estudiante: ${register.id_estudiante},
                fecha_pago: ${register.fecha_pago},
                monto_total: ${register.monto_total},
                id_padre: ${profile[0].id},
                telefono: ${profile[0].phone_number},
                cedula: ${profile[0].id_number}
            `
        );
    })

    // convertimos el array en un string para guardarlo en el pdf
    const pdfContent = registerPays.join('');

    const doc = new PDFDocument();

    doc.pipe( fs.createWriteStream('./nodejs/pdf/pays.pdf'));

    doc.fontSize(10);
    doc.text(pdfContent, 80, 100);
    doc.save();
    doc.end();

    return res.download('./nodejs/pdf/pays.pdf');
}