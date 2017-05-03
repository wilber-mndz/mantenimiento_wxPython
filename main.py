#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Agrega soporte para caracteres unicode
from __future__ import unicode_literals
import sqlite3
import wx
import wx.xrc
# Importamos el diseño de formulario
import form_main

import funciones
#Importamos formularios hijos
import ver
import insert
import update

class principal(form_main.frmPrincipal, funciones.funciones):

    def __init__(self,parent):
        #Iniciamos la clase superior
        form_main.frmPrincipal.__init__(self,parent)
        #Establecemos conexion con la base de datos
        self.conexion = sqlite3.connect("datos_empleados.db")
        self.c = self.conexion.cursor()
        print "Conexion establecida con exito "
        #Agregamos columnas al ListCtrl
        self.ListCtrl.InsertColumn(0, "id", width=30)
        self.ListCtrl.InsertColumn(1, "Nombre", width=250)
        self.ListCtrl.InsertColumn(2, "Direcion", width=240)
        self.ListCtrl.InsertColumn(3, "Edad", width=55)
        self.ListCtrl.InsertColumn(4, "DUI", width=100)
        self.ListCtrl.InsertColumn(5, "NIT", width=160)
        self.ListCtrl.InsertColumn(6, "Salario", width=90)
        self.cargar()

        #Identificaran el id del registro seleccionado
        self.item =''
        self.item2 =''

    #Lanzamos el formulario insert
    def Nuevo(self, event):
		#Instanciar ventana hija insert
        self.frmInsert = insert.MyFrame1(self)
        self.frmInsert.Show()

    def Editar(self, event):
        #Verificamos que se haya seleccionado un empleado
        if self.item2 == '':
            dialogo=wx.MessageDialog(None, 'Seleccione un empleado', 'Editar empleado', wx.OK | wx.ICON_INFORMATION)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()
        else:
            #Instanciar ventana hija editar
            self.frmUpdate = update.MyFrame1(self)
            #mostramos el formulario editar
            self.frmUpdate.Show()

    #Evento buscar del txtBuscar
    def Buscar(self, event):
        self.cargar()
        self.item2 = ''
        #print "hola"

    def Selecionar(self, event):
		self.item = self.ListCtrl.GetFocusedItem() # Obtiene la pocicion de la fila seleccionada
		self.item2 = self.ListCtrl.GetItemText(self.item)  # Trae el texto de la primer columna de la fila seleccionada
		print self.item2 #  Imprimimos id

    def Eliminar( self, event ):
        self.delete(self.item2)

    def Ver(self, event):
        if self.item2 == '':
            dialogo=wx.MessageDialog(None, 'Seleccione un empleado', 'Ver empleado', wx.OK | wx.ICON_INFORMATION)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()
        else:
            self.formSelect = ver.MyFrame1(self)
            self.formSelect.Show()

    def Cerrar(self, event):
        self.conexion.close()
        print "se cerro la conexion"
        self.Destroy()

#Instanciamos el formulario Principal
class MyApp(wx.App):
    def OnInit(self):
        frame1 = principal(None)
        self.SetTopWindow(frame1)
        frame1.Show()
        return 1

# end of class MyApp
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
