"""
Universal Serial Manager for BD
by kitiketov
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPoint

from design import Ui_MainWindow
from  handler import Handler

import sys


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.h = Handler(self.ui, self)
        

        self.setFixedSize(self.size().width(),self.size().height())
        self.setWindowTitle('Universal Serial Manager for BD')

        self.ui.editFolderPath.clicked.connect(lambda: self.h.edit_file_folder())
        self.ui.startButton.clicked.connect(lambda: self.h.start_tracking())
        self.ui.testButton.clicked.connect(lambda : self.h.test_write())
        self.ui.openPortButton.clicked.connect(lambda: self.h.openPort())
        
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

app = QtWidgets.QApplication([])
#app.setWindowIcon(QtGui.QIcon('Untitled.ico'))
application = MyWindow()
application.show()
sys.exit(app.exec())