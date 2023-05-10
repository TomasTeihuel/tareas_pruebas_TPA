from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Cartman Gets an Anal Probe / August 13, 1997 / Season 1 Episode 1")
        layout.addWidget(self.label)
        self.setLayout(layout)


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()