import path from 'path';
import mysql from 'mysql2'

export const pagLogin = (req, res) => res.sendFile(path.resolve('nodejs/public/html/login.html'));

export const userVerfication = async (req, res) => {

    const connection = await mysql.createConnection(
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

    const data = req.params.user.split('-');

    const consulta = `SELECT * FROM user WHERE name='${data[0]}' and password='${data[1]}'`

    connection.query(consulta, (err, results, fields) => {

        if (err)
            res.send('error al conectar')
        else{

            res.send(results);

            console.log(results);
        }        
    })

    connection.end();
}