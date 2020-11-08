
import sys

# PySide2 imports
from PySide2.QtWidgets import QApplication, QWidget, QPushButton

# One instance per app
app = QApplication(sys.argv)

# Our window
window = QWidget()

# Let's show our window
window.show()

# The event loop
app.exec_()
