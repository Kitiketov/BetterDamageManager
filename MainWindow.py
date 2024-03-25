"""
Universal Serial Manager for BD
by kitiketov
"""

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint
from design import Ui_MainWindow
from handler import Handler


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.h = Handler(self.ui, self)

        self.setFixedSize(self.size().width(), self.size().height())
        self.setWindowTitle('Universal Serial Manager for BD')

        self.ui.editFolderPath.clicked.connect(lambda: self.h.edit_file_folder())
        self.ui.startButton.clicked.connect(lambda: self.h.start_tracking())
        self.ui.vibroTestButton.clicked.connect(lambda: self.h.test_write(mode="vibro"))
        self.ui.shockTestButton.clicked.connect(lambda: self.h.test_write(mode="shock"))
        self.ui.openPortButton.clicked.connect(lambda: self.h.openPort())
        self.oldPos = QPoint(0, 0)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


app = QtWidgets.QApplication([])
# app.setWindowIcon(QtGui.QIcon('Untitled.ico'))
application = MyWindow()
application.show()
sys.exit(app.exec())