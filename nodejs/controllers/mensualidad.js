import mysql from 'mysql2';
import { DATABASE } from '../config.js';

// Configura la conexión a tu base de datos MySQL
const connection = mysql.createConnection(DATABASE);

function obtenerMensualidad(callback) {
    const consultaSQL = 'SELECT mensualidad FROM school_cobro LIMIT 1';
  
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
  
  export default {
    obtenerMensualidad,
    cerrarConexion,
  };