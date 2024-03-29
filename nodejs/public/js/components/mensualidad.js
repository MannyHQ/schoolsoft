
import mysql from 'mysql2';




// Configura la conexión a tu base de datos MySQL
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'school_system',
});

function obtenerMensualidad(callback) {
    const consultaSQL = 'SELECT mensualidad FROM Cobro LIMIT 1';
  
    connection.query(consultaSQL, (err, results) => {
      if (err) {
        console.error('Error al realizar la consulta:', err);
        callback(err, null);
        return;
      }
  
      if (results.length > 0) {
        const mensualidad = results[0].mensualidad;
        callback(null, mensualidad);
      } else {
        console.log('No se encontraron resultados en la tabla.');
        callback(null, null);
      }
    });
  }
  
  // Cierra la conexión a la base de datos cuando hayas terminado
  function cerrarConexion() {
    connection.end();
  }
  
  module.exports = {
    obtenerMensualidad,
    cerrarConexion,
  };