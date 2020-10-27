import sys
import braille
from UI_Principal import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, QRectF, Qt
from PySide2.QtWidgets import QMainWindow, QFileDialog, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView
from PySide2.QtGui import QPixmap

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self)

        # Inicializa la Interfaz
        self.setupUi(self)

        # Eventos de los botones ligados a sus correspondientes clases
        self.pBtn.clicked.connect(self.traducirTexto)
        self.pBtnImagen.clicked.connect(self.abrirImagen)
    
    # Clase traduccion de una cadena de texto a una cade en braille
    def traducirTexto(self):
        texto = self.txtEdit1.toPlainText()
        textoBraille = braille.textToBraille(texto)
        self.txtEdit2.setPlainText(textoBraille)

    def tr(self, text):
        return QObject.tr(self, text)

    def abrirImagen(self):
        imagen = QFileDialog.getOpenFileName(self, self.tr("Load Image"), self.tr("~/Desktop/"), self.tr("Images (*.jpg *.png)"))
        # self.label.setPixmap(QPixmap(imagen).scaled(40,40,Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label.setPixmap(QtGui.QPixmap("imagen"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
