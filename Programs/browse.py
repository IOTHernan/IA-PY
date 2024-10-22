import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Table Browser'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Crear una tabla
        self.createTable()

        # Establecer el diseño
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Mostrar la ventana
        self.show()

    def createTable(self):
        # Crear la tabla
        self.tableWidget = QTableWidget()

        # Establecer número de columnas
        self.tableWidget.setColumnCount(4)

        # Establecer número de filas
        self.tableWidget.setRowCount(4)

        # Añadir encabezados
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Nombre', 'Edad', 'Género'])

        # Añadir datos
        self.tableWidget.setItem(0, 0, QTableWidgetItem("1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Juan"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("22"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Masculino"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("2"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Ana"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("25"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("Femenino"))

        # Permitir edición de celdas
        self.tableWidget.setEditTriggers(QTableWidget.AllEditTriggers)

        # Cambiar el tamaño de las columnas para ajustarse al contenido
        self.tableWidget.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
