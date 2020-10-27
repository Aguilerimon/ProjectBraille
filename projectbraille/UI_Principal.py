# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 302)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txtEdit1 = QTextEdit(self.centralwidget)
        self.txtEdit1.setObjectName(u"txtEdit1")
        self.txtEdit1.setGeometry(QRect(250, 20, 341, 71))
        self.txtEdit2 = QTextEdit(self.centralwidget)
        self.txtEdit2.setObjectName(u"txtEdit2")
        self.txtEdit2.setGeometry(QRect(250, 110, 341, 71))
        self.pBtn = QPushButton(self.centralwidget)
        self.pBtn.setObjectName(u"pBtn")
        self.pBtn.setGeometry(QRect(400, 200, 75, 23))
        self.pBtnImagen = QPushButton(self.centralwidget)
        self.pBtnImagen.setObjectName(u"pBtnImagen")
        self.pBtnImagen.setGeometry(QRect(60, 190, 121, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 151, 131))
        self.label.setPixmap(QPixmap(u"../../../Pictures/44956558_689326568116243_8977375710507171840_n.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 616, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pBtn.setText(QCoreApplication.translate("MainWindow", u"Convertir", None))
        self.pBtnImagen.setText(QCoreApplication.translate("MainWindow", u"Abrir Imagen", None))
        self.label.setText("")
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

