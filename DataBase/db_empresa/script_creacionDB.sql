-- ============================================
-- CREAR TABLAS
-- ============================================

DROP TABLE IF EXISTS asignaciones;
DROP TABLE IF EXISTS ventas;
DROP TABLE IF EXISTS empleados;
DROP TABLE IF EXISTS proyectos;
DROP TABLE IF EXISTS departamentos;

CREATE TABLE departamentos (
    id_depto INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(100)
);

CREATE TABLE empleados (
    id_empleado INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    salario DECIMAL(10,2),
    fecha_contratacion DATE,
    id_depto INTEGER,
    FOREIGN KEY (id_depto) REFERENCES departamentos(id_depto)
);

CREATE TABLE proyectos (
    id_proyecto INTEGER PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    presupuesto DECIMAL(12,2),
    fecha_inicio DATE,
    fecha_fin DATE
);

CREATE TABLE asignaciones (
    id_asignacion INTEGER PRIMARY KEY,
    id_empleado INTEGER,
    id_proyecto INTEGER,
    horas_asignadas INT,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);

CREATE TABLE ventas (
    id_venta INTEGER PRIMARY KEY,
    id_empleado INTEGER,
    monto DECIMAL(10,2),
    fecha DATE,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
);

-- ============================================
-- INSERTAR DATOS
-- ============================================

-- Departamentos
INSERT INTO departamentos (id_depto, nombre, ubicacion) VALUES
(1,'Recursos Humanos','Santiago'),
(2,'Tecnología','Valparaíso'),
(3,'Ventas','Concepción'),
(4,'Finanzas','Santiago'),
(5,'Operaciones','Antofagasta');

-- Empleados (20 registros)
INSERT INTO empleados (id_empleado, nombre, apellido, email, salario, fecha_contratacion, id_depto) VALUES
(1,'Ana','Pérez','ana.perez@empresa.com',1500.00,'2018-01-15',1),
(2,'Luis','García','luis.garcia@empresa.com',2200.00,'2019-03-10',2),
(3,'María','Lopez','maria.lopez@empresa.com',1800.00,'2020-07-22',3),
(4,'Pedro','Martinez','pedro.martinez@empresa.com',2500.00,'2017-05-13',2),
(5,'Sofía','Ramirez','sofia.ramirez@empresa.com',3000.00,'2016-02-20',4),
(6,'Carlos','Diaz','carlos.diaz@empresa.com',1200.00,'2021-06-30',3),
(7,'Lucía','Fernandez','lucia.fernandez@empresa.com',2000.00,'2019-08-11',5),
(8,'Diego','Hernandez','diego.hernandez@empresa.com',2100.00,'2018-09-15',2),
(9,'Valentina','Castro','valentina.castro@empresa.com',1700.00,'2020-01-01',1),
(10,'Andrés','Mendoza','andres.mendoza@empresa.com',2600.00,'2017-12-12',4),
(11,'Camila','Silva','camila.silva@empresa.com',1900.00,'2022-01-10',5),
(12,'Ignacio','Morales','ignacio.morales@empresa.com',2800.00,'2016-07-07',2),
(13,'Fernanda','Reyes','fernanda.reyes@empresa.com',2300.00,'2018-04-02',3),
(14,'Matías','Torres','matias.torres@empresa.com',1500.00,'2021-03-03',5),
(15,'Daniela','Cruz','daniela.cruz@empresa.com',2100.00,'2019-10-05',4),
(16,'Felipe','Ortega','felipe.ortega@empresa.com',2400.00,'2017-11-11',2),
(17,'Josefa','Vargas','josefa.vargas@empresa.com',2700.00,'2016-06-06',1),
(18,'Tomás','Navarro','tomas.navarro@empresa.com',1600.00,'2020-02-20',3),
(19,'Isabel','Rojas','isabel.rojas@empresa.com',1950.00,'2021-04-14',5),
(20,'Cristian','Fuentes','cristian.fuentes@empresa.com',3100.00,'2015-09-09',4);

-- Proyectos (5 proyectos)
INSERT INTO proyectos (id_proyecto, nombre, presupuesto, fecha_inicio, fecha_fin) VALUES
(1,'Sistema ERP',50000.00,'2021-01-01','2022-12-31'),
(2,'Migración Nube',30000.00,'2020-06-01','2021-12-31'),
(3,'Campaña Marketing',20000.00,'2021-03-01','2021-09-30'),
(4,'Mejora Infraestructura',40000.00,'2019-01-01','2022-01-01'),
(5,'Proyecto Minería de Datos',60000.00,'2022-05-01','2023-05-01');

-- Asignaciones (50 registros)
INSERT INTO asignaciones (id_asignacion, id_empleado, id_proyecto, horas_asignadas) VALUES
(1,1,1,100),(2,2,1,120),(3,3,3,90),(4,4,2,150),(5,5,4,200),
(6,6,3,70),(7,7,5,80),(8,8,1,130),(9,9,2,60),(10,10,4,160),
(11,11,5,100),(12,12,1,140),(13,13,3,120),(14,14,5,75),(15,15,4,180),
(16,16,2,160),(17,17,1,200),(18,18,3,95),(19,19,5,85),(20,20,4,220),
(21,1,2,110),(22,2,3,80),(23,3,4,100),(24,4,5,90),(25,5,1,150),
(26,6,2,60),(27,7,3,110),(28,8,4,130),(29,9,5,70),(30,10,1,140),
(31,11,2,100),(32,12,3,120),(33,13,4,150),(34,14,5,60),(35,15,1,160),
(36,16,2,90),(37,17,3,200),(38,18,4,80),(39,19,5,110),(40,20,1,170),
(41,1,3,85),(42,2,4,140),(43,3,5,60),(44,4,1,200),(45,5,2,90),
(46,6,4,100),(47,7,1,150),(48,8,2,110),(49,9,3,95),(50,10,5,120);

-- Ventas (50 registros)
INSERT INTO ventas (id_venta, id_empleado, monto, fecha) VALUES
(1,3,500.00,'2021-01-05'),(2,6,700.00,'2021-01-10'),
(3,9,450.00,'2021-02-15'),(4,13,600.00,'2021-02-20'),
(5,18,300.00,'2021-03-01'),(6,3,800.00,'2021-03-15'),
(7,6,500.00,'2021-04-01'),(8,9,750.00,'2021-04-10'),
(9,13,900.00,'2021-05-05'),(10,18,400.00,'2021-05-20'),
(11,3,550.00,'2021-06-01'),(12,6,650.00,'2021-06-15'),
(13,9,700.00,'2021-07-01'),(14,13,500.00,'2021-07-20'),
(15,18,300.00,'2021-08-01'),(16,3,950.00,'2021-08-15'),
(17,6,400.00,'2021-09-01'),(18,9,800.00,'2021-09-10'),
(19,13,1000.00,'2021-10-05'),(20,18,450.00,'2021-10-20'),
(21,3,600.00,'2021-11-01'),(22,6,700.00,'2021-11-15'),
(23,9,500.00,'2021-12-01'),(24,13,750.00,'2021-12-20'),
(25,18,350.00,'2022-01-01'),(26,3,650.00,'2022-01-15'),
(27,6,450.00,'2022-02-01'),(28,9,900.00,'2022-02-10'),
(29,13,800.00,'2022-03-05'),(30,18,400.00,'2022-03-20'),
(31,3,550.00,'2022-04-01'),(32,6,700.00,'2022-04-15'),
(33,9,600.00,'2022-05-01'),(34,13,950.00,'2022-05-20'),
(35,18,500.00,'2022-06-01'),(36,3,750.00,'2022-06-15'),
(37,6,650.00,'2022-07-01'),(38,9,850.00,'2022-07-10'),
(39,13,1000.00,'2022-08-05'),(40,18,550.00,'2022-08-20'),
(41,3,700.00,'2022-09-01'),(42,6,600.00,'2022-09-15'),
(43,9,750.00,'2022-10-01'),(44,13,850.00,'2022-10-20'),
(45,18,400.00,'2022-11-01'),(46,3,950.00,'2022-11-15'),
(47,6,500.00,'2022-12-01'),(48,9,650.00,'2022-12-10'),
(49,13,900.00,'2023-01-05'),(50,18,450.00,'2023-01-20');
