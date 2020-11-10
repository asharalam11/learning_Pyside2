
import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclassing QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        # Calls init function of super class QMainWindow
        super().__init__()

        self.setWindowTitle("My First App")

        self.setFixedSize(QSize(400, 300))

        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked")

    def the_button_was_toggled(self, checked):
        print("Checked???? : ", checked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()

