# -*- coding: utf-8 -*-
# Base PyQt5
import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow,QApplication

from PyQt1.ui_formulario import Ui_Cuadro

# Cargar nuestro formulario *.ui
#form_class = uic.loadUiType("MiFormulario.ui")[0]
form_class = Ui_Cuadro
#Crear la Clase MyWindowClass con el formulario cargado.
class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def entrada(self):
        a = float(self.entrada1.text())
        b = float(self.entrada2.text())
        return a,b

    def salida(self,res):
        self.etresultado.setText(str(res))

 #Implementacion de los Slots referenciados en QDesigner
    def suma(self):
        v1, v2 = self.entrada()
        #v1 = float(self.entrada1.text())
        #v2 = float(self.entrada2.text())
        r = v1+v2
        self.salida(r)
        #self.etresultado.setText(str(v1+v2))

    def resta(self):
        v1, v2 = self.entrada()
        #v1 = float(self.entrada1.text())
        #v2 = float(self.entrada2.text())
        r=v1-v2
        self.salida(r)
        #self.etresultado.setText(str(v1-v2))


    def multi(self):
        v1, v2 = self.entrada()
        #v1 = float(self.entrada1.text())
        #v2 = float(self.entrada2.text())
        r=v1*v2
        self.salida(r)
        #self.etresultado.setText(str(v1*v2))


    def divi(self):
        try:
            v1, v2 = self.entrada()
            #v1 = float(self.entrada1.text())
            #v2 = float(self.entrada2.text())
            r=v1/v2
            self.salida(r)
            #self.etresultado.setText(str(v1/v2))
        except ZeroDivisionError:
            QMessageBox.warning(self,'error', 'division por cero')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()
