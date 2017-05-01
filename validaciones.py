#! /usr/bin/env python
# -*- coding: utf-8 -*-

class validaciones():

    #--------Funcion que se asegura de que el usuario solo ingrese valores entre 0 y 99
    def validar_edad(self):
        edad = str(self.txtEdad.GetValue())
        # Si el usuario engresa caracteres que no sean numeros los eliminamos
        if edad !='':
            try:
                edad = int(edad) # Verificamos que haya ingresado numeros
            except ValueError:
                lon = len(str(edad))
                edad = str(edad)[:lon -1] #Si ingreso otro tipo de valor lo eliminamos

        # Si ingresa un numero mayor a 99 eliminamos el ultimo caracter
        if len(str(edad)) > 2:
            lon = len(str(edad))
            edad = str(edad)[:lon -1]

        if str(edad) != str(self.txtEdad.GetValue()):
            self.txtEdad.SetValue(str(edad))

    #-------Funcion que se asegura que el usuario solo ingrese numeros de tipo float positivos
    def validar_salario(self):
        salario = str(self.txtSalario.GetValue())
        lon = len(str(salario))
        # Si el usuario engresa caracteres que no sean numeros los eliminamos
        if salario !='':
            if str(salario)[lon-1:] != '.' or str(salario)[lon -2:] == '..':
                #print salario
                try:
                    salario2 = float(salario)# Verificamos que haya ingresado numeros
                except ValueError:
                    salario = str(salario)[:lon -1] #Si ingreso otro tipo de valor lo eliminamos

        if str(salario) != str(self.txtSalario.GetValue()):
            self.txtSalario.SetValue(str(salario))

    # --------Nos permite validar el campo dui y darle el formato #######-#
    def validar_dui(self):
        #Funcion para validar y agragar mascara al campo DUI
        DUI = str(self.txtDUI.GetValue())
        lon = len(str(DUI))
        if lon < 9 and DUI !='':
            try:
                DUI = int(DUI) # Verificamos que haya ingresado numeros
                #print DUI
            except ValueError:
                lon = len(str(DUI))
                DUI = str(DUI)[:lon -1] #Si ingreso otro tipo de valor lo eliminamos
                self.txtDUI.SetValue(DUI)
        else:
            #Cuando hayamos ingresado los 9 digitos del dui agregamos el "-"
            if int(len(str(DUI))) == 9 and DUI[7]!="-" and DUI[8]!="-":
                DUI = DUI[0:8] + "-" + DUI[8:9]  # agregamos el "-"
                self.txtDUI.SetValue(DUI)  # Enviamos el valor al txtDUI
                self.txtNIT.SetFocus()  #Mandamos el focus al siguiente txt

    #---------Nos permite validar el campo de nit y darle formato ####-######-###-#
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

    def comprobar_campos(self):
        a = str(self.txtNombre.GetValue())
        b = str(self.txtEdad.GetValue())
        c = str(self.txtDirecion.GetValue())
        d = str(self.txtDUI.GetValue())
        e = str(self.txtNIT.GetValue())
        f = str(self.txtSalario.GetValue())

        if a == '' or b == '' or c == '' or d == '' or e == '' or f == '':
            return False
        else:
            return True
