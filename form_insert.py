# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Guardar Empleados", pos = wx.DefaultPosition, size = wx.Size( 639,461 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 9, 4, 0, 0 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 40), 1, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.txtNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer2.Add( self.txtNombre, 0, wx.ALL, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.labelEdad = wx.StaticText( self, wx.ID_ANY, u"Edad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEdad.Wrap( -1 )
		gSizer2.Add( self.labelEdad, 0, wx.ALL, 5 )

		self.txtEdad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer2.Add( self.txtEdad, 0, wx.ALL, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Direccion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.txtDirecion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer2.Add( self.txtDirecion, 0, wx.ALL, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"DUI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.txtDUI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer2.Add( self.txtDUI, 0, wx.ALL, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"NIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.txtNIT = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer2.Add( self.txtNIT, 0, wx.ALL, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Salario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.txtSalario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer2.Add( self.txtSalario, 0, wx.ALL, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnGuardar = wx.Button( self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnGuardar, 0, wx.ALL, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.txtMensaje = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtMensaje.Wrap( -1 )
		gSizer2.Add( self.txtMensaje, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.txtNombre.Bind( wx.EVT_TEXT, self.Limpiar )
		self.txtDUI.Bind( wx.EVT_TEXT, self.Mascara_DUI )
		self.txtNIT.Bind( wx.EVT_TEXT, self.Mascara_NIT )
		self.btnGuardar.Bind( wx.EVT_BUTTON, self.guardar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Limpiar( self, event ):
		event.Skip()

	def Mascara_DUI( self, event ):
		event.Skip()

	def Mascara_NIT( self, event ):
		event.Skip()

	def guardar( self, event ):
		event.Skip()
