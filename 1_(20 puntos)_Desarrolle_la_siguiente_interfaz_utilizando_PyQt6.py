
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLayout, QLineEdit, QPushButton, QMainWindow
from PyQt6.QtGui import QColor


class fefeVentana(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ventanak")
        self.setMinimumSize(600, 500)

        self.label = QLineEdit("Nombre Usuario")
        self.boton1 = QPushButton("OK")
        self.entry1 = QLineEdit("atributo 1")
        self.entry2 = QLineEdit("atributo 2")
        self.entry3 = QLineEdit("atributo 3")
        self.entry4 = QLineEdit("atributo 4")
        self.entry5 = QLineEdit("atributo 5")
        self.entry6 = QLineEdit("atributo 6")
        self.entry7 = QLineEdit("valor 1")
        self.entry8 = QLineEdit("valor 2")
        self.entry9 = QLineEdit("valor 3")
        self.entry10 = QLineEdit("valor 4")
        self.entry11 = QLineEdit("valor 5")
        self.entry12 = QLineEdit("valor 6")

        box = QVBoxLayout()

        box.addWidget(self.label)
        box.addWidget(self.entry1)
        box.addWidget(self.entry2)
        box.addWidget(self.entry3)
        box.addWidget(self.entry4)
        box.addWidget(self.entry5)
        box.addWidget(self.entry6)
        box.addWidget(self.entry7)
        box.addWidget(self.entry8)
        box.addWidget(self.entry9)
        box.addWidget(self.entry10)
        box.addWidget(self.entry11)
        box.addWidget(self.entry12)
        box.addWidget(self.boton1)

        my_window = QWidget()
        my_window.setLayout(box)
        self.setDarkMode(my_window)
        self.setDarkMode(self.entry1)
        self.setDarkMode(self.entry2)
        self.setDarkMode(self.entry3)
        self.setDarkMode(self.entry4)
        self.setDarkMode(self.entry5)
        self.setDarkMode(self.entry6)
        self.setDarkMode(self.entry7)
        self.setDarkMode(self.entry8)
        self.setDarkMode(self.entry9)
        self.setDarkMode(self.entry10)
        self.setDarkMode(self.entry11)
        self.setDarkMode(self.entry12)
        self.setDarkMode(self.boton1, 70)
        self.setCentralWidget(my_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = fefeVentana()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()