/* Creando las tablas necesarias para el usuario padre */

CREATE TABLE `Usuario` (
  `id_usuario` int(11) NOT NULL PRIMARY KEY,
  `nombre_user` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `tipo_user` int(11) NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `Estudiante` (
  `id_estudiante` int(11) NOT NULL PRIMARY KEY
  'id_padre' int(11) NOT NULL ,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `fecha_nacimiento` datetime NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `Padres` (
  `id_padre` int(11) NOT NULL PRIMARY KEY,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `cedula` varchar(11) NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `Pagos` (
  `id_pago` int(11) NOT NULL PRIMARY KEY,
  `id_padre` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `fecha_pago` datetime NOT NULL,
  `monto_total` float NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*  relacionando ordenadamenta las tablas */

ADD ALTER Pagos ADD FOREIGN KEY (id_padre) REFERENCES Padres(id_padre);