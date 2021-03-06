# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caronas.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cadastro, login, sobre, contato

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Frame da janela
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(844, 559)
        MainWindow.setFixedSize(844,559)
        MainWindow.setWindowIcon(QtGui.QIcon("Fotos/carro.jpg"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Cor da janela (ativa,inativa,desativada)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)

        #Botão para entrar na página de login
        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(270, 220, 300, 50))
        self.login.setObjectName(_fromUtf8("login"))
        self.login.clicked.connect(self.abrirlogin)

        #Botão para entrar na página de cadastro
        self.cadastro = QtGui.QPushButton(self.centralwidget)
        self.cadastro.setGeometry(QtCore.QRect(270, 290, 300, 50))
        self.cadastro.setObjectName(_fromUtf8("cadastro"))
        self.cadastro.clicked.connect(self.abrircadastro)

        #Título grande
        self.caronasinsperlabel = QtGui.QLabel(self.centralwidget)
        self.caronasinsperlabel.setGeometry(QtCore.QRect(170, 40, 521, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(60)
        self.caronasinsperlabel.setFont(font)
        self.caronasinsperlabel.setObjectName(_fromUtf8("caronasinsperlabel"))

        #Botão para abrir na página sobre nós
        self.sobre = QtGui.QPushButton(self.centralwidget)
        self.sobre.setGeometry(QtCore.QRect(270, 360, 300, 50))
        self.sobre.setObjectName(_fromUtf8("sobre"))
        self.sobre.clicked.connect(self.abrirsobre)

        #Botão para abrir a página de contato
        self.contato = QtGui.QPushButton(self.centralwidget)
        self.contato.setGeometry(QtCore.QRect(270, 430, 300, 50))
        self.contato.setObjectName(_fromUtf8("contato"))
        self.contato.clicked.connect(self.abrircontato)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Função que define os textos dentro dos botões e da janela
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        self.login.setText(_translate("MainWindow", "Login", None))
        self.cadastro.setText(_translate("MainWindow", "Cadastre-se", None))
        self.caronasinsperlabel.setText(_translate("MainWindow", "Caronas Insper", None))
        self.sobre.setText(_translate("MainWindow", "Sobre", None))
        self.contato.setText(_translate("MainWindow", "Contato", None))

    #Função para o botão: abre a página de cadastro
    def abrircadastro(self):
        self.MainWindow = cadastro.Ui_MainWindow
        tela_cadastro = QtGui.QMainWindow()
        ui = cadastro.Ui_MainWindow()
        ui.setupUi(tela_cadastro)
        tela_cadastro.show()
        sys.exit(app.exec_())

    #Função para o botão: abre a página de login
    def abrirlogin(self):
        self.MainWindow = login.Ui_MainWindow
        tela_login = QtGui.QMainWindow()
        ui = login.Ui_MainWindow()
        ui.setupUi(tela_login)
        tela_login.show()
        sys.exit(app.exec_())

    #Função para o botão: abre a página "sobre"
    def abrirsobre(self):
        self.MainWindow = sobre.Ui_MainWindow
        tela_sobre = QtGui.QMainWindow()
        ui = sobre.Ui_MainWindow()
        ui.setupUi(tela_sobre)
        tela_sobre.show()
        sys.exit(app.exec_())

    #Função para o botão: abre a página de contato
    def abrircontato(self):
        self.MainWindow = contato.Ui_MainWindow
        tela_contato = QtGui.QMainWindow()
        ui = contato.Ui_MainWindow()
        ui.setupUi(tela_contato)
        tela_contato.show()
        sys.exit(app.exec_())

#Apenas para rodar sepadaramente
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())