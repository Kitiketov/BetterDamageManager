from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QThread,QFileSystemWatcher, QIODevice
from PIL import Image,ImageGrab

import os,time



class Handler():
    def __init__(self, ui, MyWindow) -> None:
        self.ui = ui
        self.MyWindow = MyWindow

        self.path_to_txt = 'D:/Games/The Binding of Isaac Rebirth/gameinfo.txt'

        self.clipboard = QtWidgets.QApplication.clipboard()
        self.timer = QtCore.QTimer()
        self.serial = QSerialPort()
        self.serial.setBaudRate(115200)
        self.watcher = QFileSystemWatcher()
        self.portList = []
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.portList.append(port.portName())
        self.ui.comBox.addItems(self.portList)
    
    def show_message(self, widget, message=''):
        if message:
            widget.setText(message)
        widget.setEnabled(True)
        self.timer.timeout.connect(lambda: widget.setEnabled(False))
        self.timer.start(2000)

    def get_path_to_file(self):
        return QtWidgets.QFileDialog.getOpenFileName(self.MyWindow, 'выбрать путь к файлу', '', 'Текстовый документ (*.txt)')[0]

    def edit_file_folder(self):
        _path = self.get_path_to_file()
        print(_path)
        if not os.path.isfile(_path):
            self.show_message(self.ui.errorMessage, 'No file selected')
            return 'Error'
        self.path_to_txt = _path
        self.ui.folderPath.setText(self.path_to_txt)

    def test_write(self):
        with open(self.path_to_txt,"w+") as f:
            f.write(f"vibro/1/{int(time.time())}\n")

    def file_changed(self,path):
        print('File Changed: %s' % path)
        with open(self.path_to_txt) as f:
            for line in f:
                pass
        last_line = line.split("/")
        text = last_line[0]
        self.show_message(self.ui.status,text)

    def start_tracking(self):
        if not os.path.isfile(self.path_to_txt):
            self.show_message(self.ui.errorMessage, 'No file selected')
            return 'Error'
        self.watcher.addPath(self.path_to_txt)
        self.ui.editFolderPath.setEnabled(False)
        self.ui.label.setEnabled(True)
        self.watcher.fileChanged.connect(self.file_changed)

        self.swithButton(self.ui.startButton, "Stop tracking", self.stop_tracking)

    
    def stop_tracking(self):
        self.watcher.removePath(self.path_to_txt)
        self.ui.editFolderPath.setEnabled(True)
        self.ui.label.setEnabled(False)

        self.swithButton(self.ui.startButton, "Start tracking",self.start_tracking)

    def openPort(self):
        self.serial.setPortName(self.ui.comBox.currentText())
        self.serial.open(QIODevice.ReadWrite)
        self.ui.comBox.setEnabled(False)
        self.swithButton(self.ui.openPortButton, "Close port",self.closePort)

    def closePort(self):
        self.serial.close()
        self.ui.comBox.setEnabled(True)
        self.swithButton(self.ui.openPortButton, "Open port",self.openPort)


    def swithButton(self,widget,title,func):
        widget.disconnect()
        widget.setText(title)
        widget.clicked.connect(lambda: func())

    def sendSerial(self):
        self.serial.write(b'1')
        
