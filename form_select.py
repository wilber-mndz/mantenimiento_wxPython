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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Detalles Empleado", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 8, 4, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer1.AddSpacer( ( 0, 40), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.lblNombre = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNombre.Wrap( -1 )
		fgSizer1.Add( self.lblNombre, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Edad:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.lblEdad = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblEdad.Wrap( -1 )
		fgSizer1.Add( self.lblEdad, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.lblDireccion = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDireccion.Wrap( -1 )
		fgSizer1.Add( self.lblDireccion, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"DUI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.lblDui = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDui.Wrap( -1 )
		fgSizer1.Add( self.lblDui, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.NIT = wx.StaticText( self, wx.ID_ANY, u"NIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NIT.Wrap( -1 )
		fgSizer1.Add( self.NIT, 0, wx.ALL, 5 )

		self.lblNit = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNit.Wrap( -1 )
		fgSizer1.Add( self.lblNit, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Salario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.lblSalario = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblSalario.Wrap( -1 )
		fgSizer1.Add( self.lblSalario, 0, wx.ALL, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )


		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnAceptar = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnAceptar, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAceptar.Bind( wx.EVT_BUTTON, self.Aceptar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Aceptar( self, event ):
		event.Skip()
