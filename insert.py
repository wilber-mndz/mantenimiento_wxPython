#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import wx
import wx.xrc
# Importamos el diseño de formulario
import form_insert
# Importamos archivo de funciones
import funciones

#Definimos una nueva clase y heredamos los metodos de las clases importadasy
class MyFrame1(form_insert.MyFrame1, funciones.funciones):
    #constructor
    def __init__(self,parent):
		#inicializa la clase superior(parent)
        form_insert.MyFrame1.__init__(self,parent)
        self.padre = parent

        #Evento click
    def guardar( self, event ):
        self.insert()

        #Enciamos una busqueda vacia para que se actualize el formulario padre
        self.padre.txtBuscar.SetValue("")

    def Mascara_DUI(self, event):
        self.validar_dui()

    def Mascara_NIT( self, event ):
        self.validar_nit()


# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        frame1 = MyFrame1(None)
        self.SetTopWindow(frame1)
        frame1.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
