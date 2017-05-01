#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import wx
import wx.xrc

import form_select
import funciones
class MyFrame1(form_select.MyFrame1, funciones.funciones):

    def __init__(self, parent):
		#inicializa la clase superior(parent)
        form_select.MyFrame1.__init__(self,parent)
        self.conexion = sqlite3.connect("datos_empleados.db")
        print "Conexion establecida con exito "
        self.padre = parent
        self.id = self.padre.ListCtrl.GetItemText(self.padre.ListCtrl.GetFocusedItem())
        self.select(self.id)

    def Aceptar(self, event):
        self.Close()


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
