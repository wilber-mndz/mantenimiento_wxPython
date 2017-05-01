#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Class for sqlite db management 
# Author: Luis J. Aguilar
import sqlite3 

conn = sqlite3.connect('datos_empleados.db')
print "Conexion a Base de datos establecida "
c=conn.cursor()
c.execute('''CREATE TABLE empleado
       (id INT PRIMARY KEY     NOT NULL,
       dui			CHAR(12),
       nombre           TEXT   ,
       edad            INT     NOT NULL,
       direccion        CHAR(50),
       nit             CHAR(14),
       salario         REAL);''')
print "Tabla creada con exito"
conn.close()

