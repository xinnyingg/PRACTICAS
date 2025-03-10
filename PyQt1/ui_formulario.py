# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formularioVEUyHR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Cuadro(object):
    def setupUi(self, Cuadro):
        if Cuadro.objectName():
            Cuadro.setObjectName(u"Cuadro")
        Cuadro.resize(470, 255)
        self.layoutWidget = QWidget(Cuadro)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 331, 207))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.entrada1 = QLineEdit(self.layoutWidget)
        self.entrada1.setObjectName(u"entrada1")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        self.entrada1.setFont(font)

        self.verticalLayout_2.addWidget(self.entrada1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.entrada2 = QLineEdit(self.layoutWidget)
        self.entrada2.setObjectName(u"entrada2")
        self.entrada2.setFont(font)

        self.verticalLayout_2.addWidget(self.entrada2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.etresultado = QLabel(self.layoutWidget)
        self.etresultado.setObjectName(u"etresultado")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(20)
        self.etresultado.setFont(font1)

        self.verticalLayout_2.addWidget(self.etresultado)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btsuma = QPushButton(self.layoutWidget)
        self.btsuma.setObjectName(u"btsuma")

        self.verticalLayout.addWidget(self.btsuma)

        self.btresta = QPushButton(self.layoutWidget)
        self.btresta.setObjectName(u"btresta")

        self.verticalLayout.addWidget(self.btresta)

        self.btmulti = QPushButton(self.layoutWidget)
        self.btmulti.setObjectName(u"btmulti")

        self.verticalLayout.addWidget(self.btmulti)

        self.btdivi = QPushButton(self.layoutWidget)
        self.btdivi.setObjectName(u"btdivi")

        self.verticalLayout.addWidget(self.btdivi)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btsalida = QPushButton(self.layoutWidget)
        self.btsalida.setObjectName(u"btsalida")

        self.verticalLayout.addWidget(self.btsalida)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Cuadro)
        self.btsuma.clicked.connect(Cuadro.suma)
        self.btsalida.clicked.connect(Cuadro.close)
        self.btresta.clicked.connect(Cuadro.resta)
        self.btmulti.clicked.connect(Cuadro.multi)
        self.btdivi.clicked.connect(Cuadro.divi)

        QMetaObject.connectSlotsByName(Cuadro)
    # setupUi

    def retranslateUi(self, Cuadro):
        Cuadro.setWindowTitle(QCoreApplication.translate("Cuadro", u"Cuadro", None))
        self.etresultado.setText("")
        self.btsuma.setText(QCoreApplication.translate("Cuadro", u"+", None))
        self.btresta.setText(QCoreApplication.translate("Cuadro", u"-", None))
        self.btmulti.setText(QCoreApplication.translate("Cuadro", u"*", None))
        self.btdivi.setText(QCoreApplication.translate("Cuadro", u"/", None))
        self.btsalida.setText(QCoreApplication.translate("Cuadro", u"salir", None))
    # retranslateUi

