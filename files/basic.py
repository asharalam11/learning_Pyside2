
import sys

# PySide2 imports
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# One instance per app
app = QApplication(sys.argv)

# Our window
window = QMainWindow()

# Let's show our window
window.show()

# The event loop
app.exec_()
