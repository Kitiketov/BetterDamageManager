import os
from datetime import datetime, timezone

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QFileSystemWatcher, QIODevice
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo


class Handler():
    def __init__(self, ui, MyWindow) -> None:
        self.ui = ui
        self.MyWindow = MyWindow

        self.path_to_txt = ''

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
        self.ui.folderPath.setText(self.path_to_txt)
        self.last_time = int(datetime.now(timezone.utc).timestamp())
        self.last_mode = 'none'

    def show_message(self, widget, message=''):
        if message:
            widget.setText(message)
        widget.setEnabled(True)
        self.timer.timeout.connect(lambda: widget.setEnabled(False))
        self.timer.start(2000)

    def get_path_to_file(self):
        return QtWidgets.QFileDialog.getOpenFileName(self.MyWindow, 'выбрать путь к файлу', '','Текстовый документ (*.txt)')[0]

    def edit_file_folder(self):
        _path = self.get_path_to_file()
        if not os.path.isfile(_path):
            self.show_message(self.ui.errorMessage, 'No file selected')
            return 'Error'
        self.path_to_txt = _path

        self.ui.folderPath.setText(self.path_to_txt)

    def test_write(self, mode):
        if not os.path.isfile(self.path_to_txt):
            self.show_message(self.ui.errorMessage, 'No file selected')
            return 'Error'
        with open(self.path_to_txt, 'w+') as f:
            f.write(f"{mode}/1/{int(datetime.now(timezone.utc).timestamp())}\n")

    def file_changed(self, path):
        with open(self.path_to_txt) as f:
            line = f.readline()
        try:
            mode, dmg, time = line.split('/')
            ts = int(time)
            if int(dmg)<=0:
                mode = "vibro"
            if ts<=self.last_time:
                return 'Too Fast'
            if mode == 'shock':
                self.sendSerial('s', int(dmg))
            elif mode == 'vibro':
                self.sendSerial('v', int(dmg))
            elif mode == 'powerup':
                self.sendSerial('u', int(dmg))
            elif mode == 'powerdown':
                self.sendSerial('d', int(dmg))
            
            self.ui.counterDmgLabel.setText(str(int(self.ui.counterDmgLabel.text())+1))
            text = datetime.fromtimestamp(ts).strftime('%H:%M:%S ') + mode + "\n"
            self.ui.console.setPlainText(self.ui.console.toPlainText() + text)
            self.ui.console.moveCursor(QtGui.QTextCursor.End)
            self.ui.console.ensureCursorVisible()
            self.last_time = ts
        except:
            print(f'Error with line')
    def start_tracking(self):
        if not os.path.isfile(self.path_to_txt):
            self.show_message(self.ui.errorMessage, 'No file selected')
            return 'Error'
        self.watcher.addPath(self.path_to_txt)
        self.ui.editFolderPath.setEnabled(False)
        self.ui.label.setText("Online")
        self.ui.label.setEnabled(True)
        self.watcher.fileChanged.connect(self.file_changed)

        self.swithButton(self.ui.startButton, 'Stop tracking', self.stop_tracking)

    def stop_tracking(self):
        self.watcher.removePath(self.path_to_txt)
        self.ui.editFolderPath.setEnabled(True)
        self.ui.label.setText("Offline")
        self.ui.label.setEnabled(False)

        self.swithButton(self.ui.startButton, 'Start tracking', self.start_tracking)

    def openPort(self):
        self.serial.setPortName(self.ui.comBox.currentText())
        self.serial.open(QIODevice.ReadWrite)
        self.ui.comBox.setEnabled(False)
        self.swithButton(self.ui.openPortButton, 'Close port', self.closePort)

    def closePort(self):
        self.serial.close()
        self.ui.comBox.setEnabled(True)
        self.swithButton(self.ui.openPortButton, 'Open port', self.openPort)

    def swithButton(self, widget, title, func):
        widget.disconnect()
        widget.setText(title)
        widget.clicked.connect(lambda: func())

    def sendSerial(self, mode, value):
        if self.last_mode !=  mode:
            self.serial.write(f"{mode}{0}".encode())
        elif int(datetime.now(timezone.utc).timestamp())-self.last_time>=30:
            self.serial.write(f"{mode}{0}".encode())
        self.serial.write(f"{mode}{value}".encode())
        if mode not in ['u','d']:
            self.last_mode = mode
    
    def calibrating_remote_controller(self):
        self.sendSerial('v',1)
