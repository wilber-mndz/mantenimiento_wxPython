#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import wx
import wx.xrc
# Importamos el diseño de formulario
import form_update
# Importamos archivo de funciones
import funciones
import validaciones
#Definimos una nueva clase y heredamos los metodos de las clases importadasy
class MyFrame1(form_update.MyFrame1, funciones.funciones, validaciones.validaciones):
    #constructor
    def __init__(self,parent):
		#inicializa la clase superior(parent)
        form_update.MyFrame1.__init__(self,parent)
        self.padre = parent
        self.id = self.padre.ListCtrl.GetItemText(self.padre.ListCtrl.GetFocusedItem())

        print "Se actualizara el empleado con id: " + self.id
        self.cargar_por_id(self.id)


        #Evento click
    def guardar( self, event ):
        if self.comprobar_campos():
            self.update(self.id) # Actualizamos los datos del empleado
            # Enciamos eñ nombre del empleado al from principal para mostrar los cambios
            self.padre.txtBuscar.SetValue(str(self.txtNombre.GetValue()))
            self.padre.txtBuscar.SetFocus()
            self.Close()
        else:
            dialogo=wx.MessageDialog(None, 'Por favor ingrese todos los campos', 'Editar empleado', wx.OK | wx.ICON_INFORMATION)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()

    def Mascara_DUI(self, event):
        self.validar_dui()

    def Mascara_NIT( self, event ):
        self.validar_nit()

    def Validar_edad(self, event):
        self.validar_edad()

    def Validar_salario(self, event):
        self.validar_salario()


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
