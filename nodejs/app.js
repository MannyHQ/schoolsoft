const express = require("express");
const mysql = require('mysql2')

const app = express();

const connection = mysql.createConnection(
    {
        host: 'localhost',
        user: 'junior',
        password: '153wasd',
        database: 'validacion'
    }
)

connection.connect((err) => {

    if(err)
        console.log('\n<--- hubo un error --->\n', err);
    else
        console.log('conexion exitosa');
})

const consulta = `SELECT * FROM usuario`;

connection.query(consulta, (err, results, fields) => {

    if(err)
        console.log(`${err}\nhubo un error en la consulta`);
    else{

        for(const camp of results)
            console.log(`${camp.id}\n${camp.nombre}\n${camp.email}`).
        
        console.log(`consulta exitosa`);
    }
})

const PORT = process.env.PORT || 3000;
const domain = '';

app.listen(PORT, () => {

    console.log('el servidor esta escuchando');
})