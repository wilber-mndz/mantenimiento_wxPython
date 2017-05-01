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
## Class frmPrincipal
###########################################################################

class frmPrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Control de Empleados", pos = wx.DefaultPosition, size = wx.Size( 1024,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 1024,600 ), wx.DefaultSize )

		fgSizer8 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer9 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer9.AddSpacer( ( 0, 40), 1, wx.EXPAND, 5 )


		fgSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer9.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Buscar:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer9.Add( self.m_staticText4, 0, wx.ALL, 10 )

		self.txtBuscar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		fgSizer9.Add( self.txtBuscar, 0, wx.ALL, 5 )


		fgSizer9.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )


		fgSizer8.Add( fgSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer10 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer10.AddSpacer( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer10.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.ListCtrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 930,350 ), wx.LC_REPORT )
		fgSizer10.Add( self.ListCtrl, 0, wx.ALL, 5 )


		fgSizer8.Add( fgSizer10, 1, wx.EXPAND, 5 )

		fgSizer11 = wx.FlexGridSizer( 1, 5, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer11.AddSpacer( ( 100, 0), 1, wx.EXPAND, 5 )

		self.btnNuevo = wx.Button( self, wx.ID_ANY, u"Nuevo", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.btnNuevo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )

		self.btnEditar = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.btnEditar, 0, wx.ALL, 15 )

		self.btnElimiar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.btnElimiar, 0, wx.ALL, 15 )

		self.btnVer = wx.Button( self, wx.ID_ANY, u"Ver", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.btnVer, 0, wx.ALL, 15 )


		fgSizer8.Add( fgSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Cerrar )
		self.txtBuscar.Bind( wx.EVT_TEXT, self.Buscar )
		self.ListCtrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.Selecionar )
		self.btnNuevo.Bind( wx.EVT_BUTTON, self.Nuevo )
		self.btnEditar.Bind( wx.EVT_BUTTON, self.Editar )
		self.btnElimiar.Bind( wx.EVT_BUTTON, self.Eliminar )
		self.btnVer.Bind( wx.EVT_BUTTON, self.Ver )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Cerrar( self, event ):
		event.Skip()

	def Buscar( self, event ):
		event.Skip()

	def Selecionar( self, event ):
		event.Skip()

	def Nuevo( self, event ):
		event.Skip()

	def Editar( self, event ):
		event.Skip()

	def Eliminar( self, event ):
		event.Skip()

	def Ver( self, event ):
		event.Skip()
