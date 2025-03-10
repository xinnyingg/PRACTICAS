# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerDihIOq.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PPyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(1109, 831)
        self.splitter_2 = QSplitter(Calculator)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(80, 110, 275, 179))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.Valor1 = QLineEdit(self.splitter_2)
        self.Valor1.setObjectName(u"Valor1")
        font = QFont()
        font.setPointSize(16)
        self.Valor1.setFont(font)
        self.splitter_2.addWidget(self.Valor1)
        self.Valor2 = QLineEdit(self.splitter_2)
        self.Valor2.setObjectName(u"Valor2")
        self.Valor2.setFont(font)
        self.splitter_2.addWidget(self.Valor2)
        self.Resultado = QLabel(self.splitter_2)
        self.Resultado.setObjectName(u"Resultado")
        self.Resultado.setFont(font)
        self.splitter_2.addWidget(self.Resultado)
        self.splitter = QSplitter(Calculator)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(410, 60, 101, 283))
        self.splitter.setOrientation(Qt.Vertical)
        self.btnMas = QPushButton(self.splitter)
        self.btnMas.setObjectName(u"btnMas")
        self.btnMas.setFont(font)
        self.splitter.addWidget(self.btnMas)
        self.btnMenos = QPushButton(self.splitter)
        self.btnMenos.setObjectName(u"btnMenos")
        self.btnMenos.setFont(font)
        self.splitter.addWidget(self.btnMenos)
        self.btnMultiplicar = QPushButton(self.splitter)
        self.btnMultiplicar.setObjectName(u"btnMultiplicar")
        self.btnMultiplicar.setFont(font)
        self.splitter.addWidget(self.btnMultiplicar)
        self.btnDividir = QPushButton(self.splitter)
        self.btnDividir.setObjectName(u"btnDividir")
        self.btnDividir.setFont(font)
        self.splitter.addWidget(self.btnDividir)
        self.btnSalir = QPushButton(self.splitter)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setFont(font)
        self.splitter.addWidget(self.btnSalir)

        self.retranslateUi(Calculator)
        self.btnMas.clicked.connect(Calculator.suma)
        self.btnMenos.clicked.connect(Calculator.resta)
        self.btnMultiplicar.clicked.connect(Calculator.multiplicar)
        self.btnDividir.clicked.connect(Calculator.dividir)
        self.btnSalir.clicked.connect(Calculator.close)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.Resultado.setText(QCoreApplication.translate("Calculator", u"Resultado", None))
        self.btnMas.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.btnMenos.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.btnMultiplicar.setText(QCoreApplication.translate("Calculator", u"x", None))
        self.btnDividir.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.btnSalir.setText(QCoreApplication.translate("Calculator", u"Salir", None))
    # retranslateUi

