-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-10-2023 a las 17:28:11
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `registro_paciente`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto_paciente`
--

CREATE TABLE `contacto_paciente` (
  `DNI_Paciente` int(8) NOT NULL,
  `Num_celular` int(10) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Tel_alternativo` int(10) DEFAULT NULL,
  `Localidad` varchar(70) DEFAULT NULL,
  `C_P` int(4) DEFAULT NULL,
  `Correo_Electronico` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_de_paciente`
--

CREATE TABLE `datos_de_paciente` (
  `ID_PACIENTE` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `DNI` int(10) NOT NULL,
  `direccion` varchar(20) DEFAULT NULL,
  `celular` int(10) DEFAULT NULL,
  `obra_social` varchar(12) NOT NULL,
  `nombre_personal_admision` varchar(20) NOT NULL,
  `fecha_hisopado` varchar(10) DEFAULT NULL,
  `turno` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hisopados_covid`
--

CREATE TABLE `hisopados_covid` (
  `DNI_Personal_Hisopador` int(8) NOT NULL,
  `Fecha_Hisopado` date DEFAULT NULL,
  `Resultado` varchar(20) DEFAULT NULL,
  `DNI_Paciente` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historia_clinica`
--

CREATE TABLE `historia_clinica` (
  `DNI_Paciente` int(8) NOT NULL,
  `Fecha_de_Admición` date NOT NULL,
  `Fecha_Alta` date NOT NULL,
  `Medico_a_Cargo` varchar(40) NOT NULL,
  `Diagnostico` varchar(200) DEFAULT NULL,
  `Tratamiento` varchar(100) NOT NULL,
  `Notas_Medicas` varchar(200) DEFAULT NULL,
  `Resultados_de_Testeo` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `obras_sociales`
--

CREATE TABLE `obras_sociales` (
  `rnos` int(10) NOT NULL,
  `denominacion` varchar(100) NOT NULL,
  `siglas` varchar(20) DEFAULT NULL,
  `domicilio` varchar(50) DEFAULT NULL,
  `localidad` varchar(50) DEFAULT NULL,
  `cp` int(4) DEFAULT NULL,
  `provincia` varchar(20) DEFAULT NULL,
  `telefono` int(10) DEFAULT NULL,
  `otros_telefonos` int(40) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `web` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `Nombres` varchar(50) NOT NULL,
  `Apellidos` varchar(50) NOT NULL,
  `DNI` int(8) NOT NULL,
  `Fecha_Nacimiento` date DEFAULT NULL,
  `Id_Obra_Social` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `DNI_Personal` int(8) NOT NULL,
  `Apellidos` varchar(30) DEFAULT NULL,
  `Nombres` varchar(30) DEFAULT NULL,
  `Area` varchar(20) DEFAULT NULL,
  `telefono` int(10) DEFAULT NULL,
  `direccion` varchar(80) DEFAULT NULL,
  `e_mail` varchar(50) DEFAULT NULL,
  `cp` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tratamiento_covid`
--

CREATE TABLE `tratamiento_covid` (
  `Tipos_de_Tratamientos` varchar(100) NOT NULL,
  `Fecha_de_Inicio` date NOT NULL,
  `Fecha_de_Finalización` date NOT NULL,
  `Medicamentos` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `contacto_paciente`
--
ALTER TABLE `contacto_paciente`
  ADD PRIMARY KEY (`DNI_Paciente`);

--
-- Indices de la tabla `datos_de_paciente`
--
ALTER TABLE `datos_de_paciente`
  ADD PRIMARY KEY (`ID_PACIENTE`);

--
-- Indices de la tabla `hisopados_covid`
--
ALTER TABLE `hisopados_covid`
  ADD PRIMARY KEY (`DNI_Personal_Hisopador`),
  ADD KEY `DNI_Paciente` (`DNI_Paciente`),
  ADD KEY `Resultado` (`Resultado`);

--
-- Indices de la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  ADD PRIMARY KEY (`DNI_Paciente`),
  ADD KEY `Tratamiento` (`Tratamiento`),
  ADD KEY `Resultados_de_Testeo` (`Resultados_de_Testeo`);

--
-- Indices de la tabla `obras_sociales`
--
ALTER TABLE `obras_sociales`
  ADD PRIMARY KEY (`rnos`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`DNI`),
  ADD KEY `Id_Obra_Social` (`Id_Obra_Social`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`DNI_Personal`);

--
-- Indices de la tabla `tratamiento_covid`
--
ALTER TABLE `tratamiento_covid`
  ADD PRIMARY KEY (`Tipos_de_Tratamientos`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos_de_paciente`
--
ALTER TABLE `datos_de_paciente`
  MODIFY `ID_PACIENTE` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `hisopados_covid`
--
ALTER TABLE `hisopados_covid`
  ADD CONSTRAINT `hisopados_covid_ibfk_1` FOREIGN KEY (`DNI_Personal_Hisopador`) REFERENCES `personal` (`DNI_Personal`),
  ADD CONSTRAINT `hisopados_covid_ibfk_2` FOREIGN KEY (`Resultado`) REFERENCES `historia_clinica` (`Resultados_de_Testeo`);

--
-- Filtros para la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  ADD CONSTRAINT `historia_clinica_ibfk_1` FOREIGN KEY (`DNI_Paciente`) REFERENCES `paciente` (`DNI`),
  ADD CONSTRAINT `historia_clinica_ibfk_2` FOREIGN KEY (`Tratamiento`) REFERENCES `tratamiento_covid` (`Tipos_de_Tratamientos`);

--
-- Filtros para la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD CONSTRAINT `paciente_ibfk_1` FOREIGN KEY (`DNI`) REFERENCES `contacto_paciente` (`DNI_Paciente`),
  ADD CONSTRAINT `paciente_ibfk_2` FOREIGN KEY (`Id_Obra_Social`) REFERENCES `obras_sociales` (`rnos`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
