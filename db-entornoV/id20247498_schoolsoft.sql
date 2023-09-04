-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 13-08-2023 a las 18:57:27
-- Versión del servidor: 10.5.20-MariaDB
-- Versión de PHP: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `id20247498_schoolsoft`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Asignatura`
--

CREATE TABLE `Asignatura` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `nivel` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='datos asignaturas';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Calificaciones`
--

CREATE TABLE `Calificaciones` (
  `id` int(11) NOT NULL,
  `estudiante_id` int(11) NOT NULL,
  `asignatura_id` int(11) NOT NULL,
  `maestro_id` int(11) NOT NULL,
  `calificacion` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='calificaciones estudiantes';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Calificaciones_Destacadas`
--

CREATE TABLE `Calificaciones_Destacadas` (
  `id` int(11) NOT NULL,
  `nombre_Estud` varchar(50) NOT NULL,
  `apellido_Estud` varchar(100) NOT NULL,
  `calific_Estud` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `Maestro_id` int(11) NOT NULL,
  `curso_id` int(11) NOT NULL,
  `Asignatura_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Calificaciones Destacadas(para tabla)';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Calificaciones_Periodos`
--

CREATE TABLE `Calificaciones_Periodos` (
  `id_estudiante` int(11) NOT NULL,
  `nombre_estudiante` varchar(50) NOT NULL,
  `id_asignatura` int(11) NOT NULL,
  `calificacion1` tinyint(4) NOT NULL,
  `calificacion2` tinyint(4) NOT NULL,
  `calificacion_total` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `chat`
--

CREATE TABLE `chat` (
  `id_estudiante` int(11) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `texto` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='puede sufrir actualizacion en un futuro';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Curso`
--

CREATE TABLE `Curso` (
  `id_curso` int(11) NOT NULL,
  `nivel` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Estudiante`
--

CREATE TABLE `Estudiante` (
  `id_estudiante` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `fecha_nacimiento` datetime NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Inscripcion`
--

CREATE TABLE `Inscripcion` (
  `id_inscripcion` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `Id_curso` int(11) NOT NULL,
  `fecha_ins` datetime NOT NULL DEFAULT current_timestamp(),
  `estado_pago` bit(1) NOT NULL,
  `ref_pago` int(11) NOT NULL,
  `estado_ins` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Maestros`
--

CREATE TABLE `Maestros` (
  `id` int(11) NOT NULL COMMENT 'key primary',
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `matricula` varchar(100) NOT NULL,
  `cedula` int(11) NOT NULL COMMENT 'identificacion',
  `signatura_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Datos de los maestros';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mjs_privado_maestro`
--

CREATE TABLE `mjs_privado_maestro` (
  `id_estudiante` int(11) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `asunto` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Notes_maestro`
--

CREATE TABLE `Notes_maestro` (
  `id` int(11) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `note` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Padres`
--

CREATE TABLE `Padres` (
  `id_padre` FOREIGN KEY int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `cedula` varchar(11) NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Pagos`
--

CREATE TABLE `Pagos` (
  `id_pago` int(11) NOT NULL,
  `id_padre` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `fecha_pago` datetime NOT NULL,
  `monto_total` float NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Tipo_Usuario`
--

CREATE TABLE `Tipo_Usuario` (
  `id_tipo` int(11) NOT NULL,
  `tipo_usuario` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Trabajo_fijado_maestro`
--

CREATE TABLE `Trabajo_fijado_maestro` (
  `id` int(11) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `trabajo` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuario`
--

CREATE TABLE `Usuario` (
  PRIMARY KEY `id_usuario` int(11) NOT NULL,
  `nombre_user` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `tipo_user` int(11) NOT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Asignatura`
--
ALTER TABLE `Asignatura`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Calificaciones`
--
ALTER TABLE `Calificaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `asignatura_id` (`asignatura_id`),
  ADD KEY `estudiante_id` (`estudiante_id`),
  ADD KEY `maestro_id` (`maestro_id`);

--
-- Indices de la tabla `Calificaciones_Destacadas`
--
ALTER TABLE `Calificaciones_Destacadas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Asignatura_id` (`Asignatura_id`),
  ADD KEY `curso_id` (`curso_id`),
  ADD KEY `Maestro_id` (`Maestro_id`);

--
-- Indices de la tabla `chat`
--
ALTER TABLE `chat`
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_maestro` (`id_maestro`);

--
-- Indices de la tabla `Curso`
--
ALTER TABLE `Curso`
  ADD PRIMARY KEY (`id_curso`);

--
-- Indices de la tabla `Estudiante`
--
ALTER TABLE `Estudiante`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- Indices de la tabla `Inscripcion`
--
ALTER TABLE `Inscripcion`
  ADD PRIMARY KEY (`id_inscripcion`);

--
-- Indices de la tabla `Maestros`
--
ALTER TABLE `Maestros`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unica_matricula` (`matricula`),
  ADD UNIQUE KEY `unica_cedula` (`cedula`),
  ADD UNIQUE KEY `fk` (`signatura_id`),
  ADD KEY `signatura_id` (`signatura_id`);

--
-- Indices de la tabla `mjs_privado_maestro`
--
ALTER TABLE `mjs_privado_maestro`
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_maestro` (`id_maestro`);

--
-- Indices de la tabla `Notes_maestro`
--
ALTER TABLE `Notes_maestro`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_maestro` (`id_maestro`);

--
-- Indices de la tabla `Padres`
--
ALTER TABLE `Padres`
  ADD PRIMARY KEY (`id_padre`);

--
-- Indices de la tabla `Pagos`
--
ALTER TABLE `Pagos`
  ADD PRIMARY KEY (`id_pago`);

--
-- Indices de la tabla `Tipo_Usuario`
--
ALTER TABLE `Tipo_Usuario`
  ADD PRIMARY KEY (`id_tipo`);

--
-- Indices de la tabla `Trabajo_fijado_maestro`
--
ALTER TABLE `Trabajo_fijado_maestro`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_maestro` (`id_maestro`);

--
-- Indices de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Curso`
--
ALTER TABLE `Curso`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Estudiante`
--
ALTER TABLE `Estudiante`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Inscripcion`
--
ALTER TABLE `Inscripcion`
  MODIFY `id_inscripcion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Padres`
--
ALTER TABLE `Padres`
  MODIFY `id_padre` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Pagos`
--
ALTER TABLE `Pagos`
  MODIFY `id_pago` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Tipo_Usuario`
--
ALTER TABLE `Tipo_Usuario`
  MODIFY `id_tipo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Calificaciones`
--
ALTER TABLE `Calificaciones`
  ADD CONSTRAINT `Calificaciones_ibfk_1` FOREIGN KEY (`asignatura_id`) REFERENCES `Asignatura` (`id`),
  ADD CONSTRAINT `Calificaciones_ibfk_2` FOREIGN KEY (`estudiante_id`) REFERENCES `Estudiante` (`id_estudiante`),
  ADD CONSTRAINT `Calificaciones_ibfk_3` FOREIGN KEY (`maestro_id`) REFERENCES `Maestros` (`id`);

--
-- Filtros para la tabla `Calificaciones_Destacadas`
--
ALTER TABLE `Calificaciones_Destacadas`
  ADD CONSTRAINT `Calificaciones_Destacadas_ibfk_1` FOREIGN KEY (`Asignatura_id`) REFERENCES `Asignatura` (`id`),
  ADD CONSTRAINT `Calificaciones_Destacadas_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `Curso` (`id_curso`),
  ADD CONSTRAINT `Calificaciones_Destacadas_ibfk_3` FOREIGN KEY (`Maestro_id`) REFERENCES `Maestros` (`id`);

--
-- Filtros para la tabla `chat`
--
ALTER TABLE `chat`
  ADD CONSTRAINT `chat_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `Estudiante` (`id_estudiante`),
  ADD CONSTRAINT `chat_ibfk_2` FOREIGN KEY (`id_maestro`) REFERENCES `Maestros` (`id`);

--
-- Filtros para la tabla `Maestros`
--
ALTER TABLE `Maestros`
  ADD CONSTRAINT `Maestros_ibfk_1` FOREIGN KEY (`signatura_id`) REFERENCES `Asignatura` (`id`);

--
-- Filtros para la tabla `mjs_privado_maestro`
--
ALTER TABLE `mjs_privado_maestro`
  ADD CONSTRAINT `mjs_privado_maestro_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `Estudiante` (`id_estudiante`),
  ADD CONSTRAINT `mjs_privado_maestro_ibfk_2` FOREIGN KEY (`id_maestro`) REFERENCES `Maestros` (`id`);

--
-- Filtros para la tabla `Notes_maestro`
--
ALTER TABLE `Notes_maestro`
  ADD CONSTRAINT `Notes_maestro_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `Maestros` (`id`);

--
-- Filtros para la tabla `Trabajo_fijado_maestro`
--
ALTER TABLE `Trabajo_fijado_maestro`
  ADD CONSTRAINT `Trabajo_fijado_maestro_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `Maestros` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
