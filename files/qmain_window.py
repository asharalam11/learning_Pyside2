
import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclassing QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        # Calls init function of super class QMainWindow
        super().__init__()

        self.setWindowTitle("My First App")

        button = QPushButton("Press me!")

        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()

