import sys
import braille
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile

class uiprincipal ():
    def __init__(self):
        super(uiprincipal, self).__init__()
        self.ui = QUiLoader().load(QFile("UI_Principal.ui")) 
        self.ui.pBtn.clicked.connect(self.traducirTexto)
    
    def traducirTexto(self):
        texto = self.ui.txtEdit1.toPlainText()
        textoBraille = braille.textToBraille(texto)
        self.ui.txtEdit2.setPlainText(textoBraille)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp= uiprincipal()
    myapp.ui.show()
    sys.exit(app.exec_())
