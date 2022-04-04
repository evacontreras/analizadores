import sys

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui

""" Importamos todas nuetras Ventana y funciones utiles"""
from vista.home import  *
from analizador_lexico import *
from analizador_sintactico import *

class Main(QMainWindow):
    """ Clase principal de nuestra app"""
    def __init__(self):
        """ Incializamos nuestra app"""
        QMainWindow.__init__(self)


        self.home = Ui_home()
        self.home.setupUi(self)

        # Eventos
        self.home.bt_lexico.clicked.connect(self.ev_lexico)
        self.home.bt_sintactico.clicked.connect(self.ev_sintactico)

        self.home.bt_archivo.clicked.connect(self.ev_archivo)
        self.home.bt_limpiar.clicked.connect(self.ev_limpiar)


        self.home.estado.showMessage("Guerra Gonzalez y brian alexis")

    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        :return: 
        '''

        self.home.tx_lexico.setText('')


        datos = self.home.tx_ingreso.toPlainText().strip()


        resultado_lexico = prueba(datos)


        cadena= ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.home.tx_lexico.setText(cadena)


    def ev_sintactico(self):
        '''
        Manejo de analisis gramatico
        :return: 
        '''

        self.home.tx_sintactico.setText('')

        datos = self.home.tx_ingreso.toPlainText().strip()


        resultado_sintactico = prueba_sintactica(datos)
        cadena = ''


        for item in resultado_sintactico:
            cadena += item + "\n"

        self.home.tx_sintactico.setText( cadena )

    def ev_archivo(self):
        '''
        Manejo de subir archivo 
        :return: 
        '''
        dlg = QFileDialog()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read().strip()
                if data:
                    self.home.tx_ingreso.setText(data+"\n")

    def ev_limpiar(self):
        '''
        Manejo de limpieza de campos
        :return: 
        '''
        self.home.tx_ingreso.setText('')
        self.home.tx_lexico.setText('')
        self.home.tx_sintactico.setText('')




def iniciar():

    app = QApplication(sys.argv)


    ventana = Main()

    ventana.show()


    sys.exit(app.exec_())


if __name__ == '__main__':
    iniciar()
