-- CREATE TABLE `Tarjeta` (
--     `id_padre` : int(11) NOT NULL,
--     `numero` : varchar(16) NOT NULL,
--     `cvv` : int(3) NOT NULL,
--     `fecha_venc` : varchar(5) NOT NULL

-- )

-- CREATE TABLE `Estudiante` (
--     `first_name` varchar(200) NOT NULL,
--     `last_name` varchar(200) NOT NULL,
--     `birthdate` DateTime NOT NULL,
--     `gender` varchar(11) NOT NULL,
--     `id_number` int(11) NOT NULL,
--     `mail` varchar(200) NOT NULL,
--     `phone_number` varchar(13) NOT NULL,
--     `status` bit(1) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- CREATE TABLE `Padres` (
--   `id_padre` int(11) NOT NULL,
--   `nombre` varchar(50) NOT NULL,
--   `apellido` varchar(50) NOT NULL,
--   `correo` varchar(50) NOT NULL,
--   `telefono` bigint(20) NOT NULL,
--   `cedula` varchar(11) NOT NULL,
--   `estado` bit(1) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- CREATE TABLE `Pagos` (
--   `id_pago` int(11) NOT NULL,
--   `id_padre` int(11) NOT NULL,
--   `id_estudiante` int(11) NOT NULL,
--   `fecha_pago` datetime NOT NULL,
--   `monto_total` float NOT NULL,
--   `estado` bit(1) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- CREATE TABLE `Usuario` (
--   `id_usuario` int(11) NOT NULL,
--   `nombre_user` varchar(50) NOT NULL,
--   `password` varchar(50) NOT NULL,
--   `correo` varchar(50) NOT NULL,
--   `tipo_user` int(11) NOT NULL,
--   `estado` bit(1) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;