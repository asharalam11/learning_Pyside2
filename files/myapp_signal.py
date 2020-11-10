
import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclassing QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        # Calls init function of super class QMainWindow
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My First App")

        self.setFixedSize(QSize(400, 300))

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Monitoring state: ", self.button_is_checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()

