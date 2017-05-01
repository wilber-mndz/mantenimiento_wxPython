import sqlite3
import wx
import wx.xrc
# Funcion que optiene el ultimo id insertado en una tabla y le suma 1
# usa como parametros el nombre de la base de datos, nombre de la tabla y id
class funciones():
    #Funcion para autoimcrementar el id de una tabla
    def id_auto_increment(self, db_name, tbl_name, id_name ):
        #Establecemos la conexion a la base de datos
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        # Obtenesmos el ultimo registro ingresado la Tabla
        c.execute("SELECT " + id_name + " FROM " + tbl_name + " ORDER BY " + id_name + " DESC LIMIT 1")
        resultado = c.fetchall()  # Almasenamos el resultado de la consulta
        #Si encontro un registro
        if len(resultado) != 0:
            last_id = int(resultado[0][0]) + 1  # Le sumamos 1 al ultimo id optenido
            #print last_id
            return last_id  #retornamos el nuevo id
        else:
            # Si no hay registros el primer id es 1
            return 1

    #Nos permite validar el campo dui y darle el formato #######-#
    def validar_dui(self):
        #Funcion para validar y agragar mascara al campo DUI
        DUI = str(self.txtDUI.GetValue())
        #Cuando hayamos ingresado los 9 digitos del dui agregamos el "-"
        if int(len(DUI)) == 9 and DUI[7]!="-" and DUI[8]!="-":
            DUI = DUI[0:8] + "-" + DUI[8:9]  # agregamos el "-"
            self.txtDUI.SetValue(DUI)  # Enviamos el valor al txtDUI
            self.txtNIT.SetFocus()  #Mandamos el focus al siguiente txt

    #Nos permite validar el campo de nit y darle formato ####-######-###-#
    def validar_nit(self):
        NIT = str(self.txtNIT.GetValue())

        # Si el usuaio quiere corregir el dato quitamos los "-" que agregamos
        if int(len(NIT)) !=17:
            NIT = (str(NIT)).replace("-","") #Eliminamos los "-"
            #print NIT

        if int(len(NIT)) == 14 and NIT[4]!="-" and NIT[13]!="-" and NIT[12]!="-":
            NIT = NIT[0:4] + "-" + NIT[4:10] + "-" + NIT[10:13] + "-" + NIT[13:14]
            self.txtSalario.SetFocus()

        if str(NIT) != str(self.txtNIT.GetValue()):
            self.txtNIT.SetValue(NIT)

    #Funcion que nos permite registrar un nuevo empleado
    def insert(self):
        # Optenemos el id que ingresaremos
        self.conexion = sqlite3.connect("datos_empleados.db")
        #print "Conexion establecida con exito "
        id = self.id_auto_increment("datos_empleados.db", "empleado", "id")
        #print "id del registro " + str(id)
        # Capturamos lo valores de los txt
        nombre = str(self.txtNombre.GetValue())
        edad = str(self.txtEdad.GetValue())
        direccion = str(self.txtDirecion.GetValue())
        dui = str(self.txtDUI.GetValue())
        nit = str(self.txtNIT.GetValue())
        salario = str(self.txtSalario.GetValue())
        # Insertamos Registro en la base de datos
        c=self.conexion.cursor()
        c.execute("INSERT INTO empleado VALUES (?,?,?,?,?,?,?)",(id,dui,nombre,edad,direccion,nit,salario))
        self.conexion.commit()
        self.conexion.close()
        #print "Conexion cerrada"

        #Limpiamos TextCtrl para realizar un nuevo registro
        self.txtNombre.SetValue("")
        self.txtEdad.SetValue("")
        self.txtDirecion.SetValue("")
        self.txtDUI.SetValue("")
        self.txtNIT.SetValue("")
        self.txtSalario.SetValue("")
        self.txtNombre.SetFocus()

        #Generamos un cuadro de dialogo que indique los cambios
        dialogo=wx.MessageDialog(None, 'Datos guardados correctamente\n Id: '+str(id)+'', 'Guardar empleado', wx.OK | wx.ICON_INFORMATION)
        respuesta = dialogo.ShowModal()
        dialogo.Destroy()

        #Pregunta si decea registrar otro empleado si no se haran mas registros cerrar formulario
        #Deshabilitado porque envia el formulario de registro al fondo
        # dialogo2=wx.MessageDialog(None, 'Decea registrar otro empleado?', 'Guardar empleado', wx.YES_NO | wx.ICON_INFORMATION)
        # otro = dialogo2.ShowModal()
        # if otro == wx.ID_YES:
        #     dialogo2.Destroy()
        # else:
        #     dialogo2.Destroy()
        #     self.Close()

    def update(self, id):
        self.conexion = sqlite3.connect("datos_empleados.db")
        print "Conexion establecida con exito "
        c = self.conexion.cursor()
        nombre = str(self.txtNombre.GetValue())
        edad = str(self.txtEdad.GetValue())
        direccion = str(self.txtDirecion.GetValue())
        dui = str(self.txtDUI.GetValue())
        nit = str(self.txtNIT.GetValue())
        salario = str(self.txtSalario.GetValue())
        c.execute("UPDATE empleado SET dui='"+dui+"', nombre='"+nombre+"', edad='"+edad+"', direccion='"+direccion+"', nit='"+nit+"', salario='"+salario+"' WHERE id = '"+id+"'")
        self.conexion.commit()
        self.conexion.close()

        #Generamos un cuadro de dialogo que indique los cambios
        dialogo=wx.MessageDialog(None, 'Datos guardados correctamente', 'Editar empleado', wx.OK | wx.ICON_INFORMATION)
        respuesta = dialogo.ShowModal()
        dialogo.Destroy()

    def delete(self, id):
        if id == '':
            dialogo=wx.MessageDialog(None, 'Seleccione un empleado', 'Eliminar empleado', wx.OK | wx.ICON_INFORMATION)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()
        else:
            dialogo=wx.MessageDialog(None, 'Decea eliminar este empleado?', 'Eliminar empleado', wx.YES_NO | wx.ICON_INFORMATION)
            respuesta = dialogo.ShowModal()
            if respuesta == wx.ID_YES:
                dialogo.Destroy()
                c = self.conexion.cursor()
                c.execute("DELETE FROM empleado WHERE id = '"+id+"'")
                self.conexion.commit()
                # Guardamos el valor de la busqueda actual
                busqueda = str(self.txtBuscar.GetValue())
                self.txtBuscar.SetValue(busqueda) #Actualizamos la busqueda
                #Generamos un cuadro de dialogo que indique los cambios
                dialogo=wx.MessageDialog(None, 'Se a eliminado el registro', 'Eliminar empleado', wx.OK | wx.ICON_INFORMATION)
                respuesta = dialogo.ShowModal()
                dialogo.Destroy()
            else:
                dialogo.Destroy()

    #Funcion para mostrar los datos del usuario en el formulario "Ver"
    def select(self, id):
        self.conexion = sqlite3.connect("datos_empleados.db")
        c = self.conexion.cursor()
        c.execute("SELECT * FROM empleado WHERE id = '"+id+"'")
        resultado = c.fetchone()
        self.conexion.close()

        self.lblNombre.SetLabel(resultado[2])
        self.lblEdad.SetLabel(str(resultado[3]))
        self.lblDireccion.SetLabel(str(resultado[4]))
        self.lblDui.SetLabel(str(resultado[1]))
        self.lblNit.SetLabel(str(resultado[5]))
        self.lblSalario.SetLabel(str(resultado[6]))

    #Optiene los datos de un empleado en la ventana editar
    def cargar_por_id(self, id):
        self.conexion = sqlite3.connect("datos_empleados.db")
        c = self.conexion.cursor()
        c.execute("SELECT * FROM empleado WHERE id = '"+id+"'")
        resultado = c.fetchone()
        self.conexion.close()
        self.txtNombre.SetValue(resultado[2])
        self.txtEdad.SetValue(str(resultado[3]))
        self.txtDirecion.SetValue(str(resultado[4]))
        self.txtDUI.SetValue(str(resultado[1]))
        self.txtNIT.SetValue(str(resultado[5]))
        self.txtSalario.SetValue(str(resultado[6]))

    # Funcion para cargar los empleados desde la base de datos en la ventana principal
    def cargar(self):

        self.ListCtrl.DeleteAllItems()
        #Optenemos el valor para realizar la busqueda
        busqueda = self.txtBuscar.GetValue()

        # Si el usuario escribio una busqueda
        if busqueda!="":
            self.c.execute("SELECT * FROM empleado WHERE nombre like '%"+str(busqueda)+"%' ORDER BY id DESC")
            resultado= self.c.fetchall()
            #print resultado
        else: # Si la busqueda esta vacia traemos todos los registros
            self.c.execute("SELECT * FROM empleado ORDER BY id DESC")
            resultado = self.c.fetchall()
            #print resultado

        rows = 0 # Lleva el conteo de las filas insertadas

        #Llenamos el ListControl
        for empleado in resultado:
            # Insertamos nustra fila con el primer elemento en el indice 0
            self.ListCtrl.InsertStringItem(rows, str(empleado[0]))
            # insertamos nuestro elemento en la columna siguiente (fila, columna, str)
            self.ListCtrl.SetStringItem(rows,1, str(empleado[2]))
            self.ListCtrl.SetStringItem(rows,2, str(empleado[4]))
            self.ListCtrl.SetStringItem(rows,3, str(empleado[3]))
            self.ListCtrl.SetStringItem(rows,4, str(empleado[1]))
            self.ListCtrl.SetStringItem(rows,5, str(empleado[5]))
            self.ListCtrl.SetStringItem(rows,6, str(empleado[6]))
