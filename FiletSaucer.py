# FiletSaucer.py

NAME = "FiletSaucer"
VERSION = "0.2.0"
REPOSITORY = "https://github.com/Mikumikunisiteageru/FiletSaucer"

CONFIG = "FiletSaucer_config.ini"

import datetime
import glob
import os
import re
import shutil
import sys
import time
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 200, 126))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 126, 200, 474))
        self.widget.setObjectName("widget")
        self.pushButton_01 = QtWidgets.QPushButton(self.widget)
        self.pushButton_01.setGeometry(QtCore.QRect(0, 0, 200, 135))
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_02 = QtWidgets.QPushButton(self.widget)
        self.pushButton_02.setGeometry(QtCore.QRect(0, 135, 120, 113))
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_03 = QtWidgets.QPushButton(self.widget)
        self.pushButton_03.setGeometry(QtCore.QRect(120, 135, 80, 113))
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_04 = QtWidgets.QPushButton(self.widget)
        self.pushButton_04.setGeometry(QtCore.QRect(0, 248, 81, 84))
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_05 = QtWidgets.QPushButton(self.widget)
        self.pushButton_05.setGeometry(QtCore.QRect(81, 248, 65, 84))
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_06 = QtWidgets.QPushButton(self.widget)
        self.pushButton_06.setGeometry(QtCore.QRect(146, 248, 54, 84))
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_07 = QtWidgets.QPushButton(self.widget)
        self.pushButton_07.setGeometry(QtCore.QRect(0, 332, 75, 51))
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_08 = QtWidgets.QPushButton(self.widget)
        self.pushButton_08.setGeometry(QtCore.QRect(75, 332, 66, 51))
        self.pushButton_08.setObjectName("pushButton_08")
        self.pushButton_09 = QtWidgets.QPushButton(self.widget)
        self.pushButton_09.setGeometry(QtCore.QRect(141, 332, 59, 51))
        self.pushButton_09.setObjectName("pushButton_09")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 383, 57, 48))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setGeometry(QtCore.QRect(57, 383, 52, 48))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setGeometry(QtCore.QRect(109, 383, 47, 48))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_13.setGeometry(QtCore.QRect(156, 383, 44, 48))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_14.setGeometry(QtCore.QRect(0, 431, 45, 43))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget)
        self.pushButton_15.setGeometry(QtCore.QRect(45, 431, 43, 43))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget)
        self.pushButton_16.setGeometry(QtCore.QRect(88, 431, 39, 43))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.widget)
        self.pushButton_17.setGeometry(QtCore.QRect(127, 431, 38, 43))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget)
        self.pushButton_18.setGeometry(QtCore.QRect(165, 431, 35, 43))
        self.pushButton_18.setObjectName("pushButton_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FiletSaucer"))
        self.pushButton_01.setText(_translate("MainWindow", "1"))
        self.pushButton_02.setText(_translate("MainWindow", "2"))
        self.pushButton_03.setText(_translate("MainWindow", "3"))
        self.pushButton_04.setText(_translate("MainWindow", "4"))
        self.pushButton_05.setText(_translate("MainWindow", "5"))
        self.pushButton_06.setText(_translate("MainWindow", "6"))
        self.pushButton_07.setText(_translate("MainWindow", "7"))
        self.pushButton_08.setText(_translate("MainWindow", "8"))
        self.pushButton_09.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "10"))
        self.pushButton_11.setText(_translate("MainWindow", "11"))
        self.pushButton_12.setText(_translate("MainWindow", "12"))
        self.pushButton_13.setText(_translate("MainWindow", "13"))
        self.pushButton_14.setText(_translate("MainWindow", "14"))
        self.pushButton_15.setText(_translate("MainWindow", "15"))
        self.pushButton_16.setText(_translate("MainWindow", "16"))
        self.pushButton_17.setText(_translate("MainWindow", "17"))
        self.pushButton_18.setText(_translate("MainWindow", "18"))

def getValue(settings, key, default):
    value = settings.value(key)
    if value == None:
        return default
    else:
        return value

def readSettings(ui):
    ui.settings = QtCore.QSettings(CONFIG, QtCore.QSettings.IniFormat)
    ui.filePattern = getValue(ui.settings, "FILE/pattern", ".*")
    ui.pathSource = getValue(ui.settings, "PATH/source", ".")
    ui.pathTarget = getValue(ui.settings, "PATH/target", ".")
    ui.position = getValue(ui.settings, "WINDOW/position", QtCore.QPoint(10, 200))
    ui.regexes = []
    i = 0
    while True:
        i += 1
        s = getValue(ui.settings, f"REGEX/s_{i}", None)
        t = getValue(ui.settings, f"REGEX/t_{i}", None)
        if s == None or t == None:
            break
        ui.regexes.append((s, t))
    print(ui.regexes)

def getPrefix(ui):
    prefix = ui.plainTextEdit.toPlainText().strip()
    for (s, t) in ui.regexes:
        prefix = re.sub(s, t, prefix)
    return prefix

def matchesPattern(ui, filename):
    body = os.path.split(filename)[-1]
    return re.match(ui.filePattern, body) != None

def getLatestFiles(ui, num):
    path = ui.pathSource
    files = glob.glob(os.path.join(path, "*"))
    newestFiles = sorted(files, key=os.path.getctime, reverse=True)[:num]
    if all(matchesPattern(ui, f) for f in newestFiles):
        return newestFiles
    else:
        raise Exception("wrong files")

def addPrefix(ui, filename, prefix):
    _, name = os.path.split(filename)
    pathTarget = os.path.join(ui.pathTarget, datetime.date.today().strftime("%Y%m"))
    if not os.path.isdir(pathTarget):
        raise Exception("wrong target path")
    if prefix == "":
        newName = os.path.join(pathTarget, name)
    else:
        newName = os.path.join(pathTarget, prefix + "_" + name)
    if os.path.isfile(newName):
        raise Exception("file exists")
    shutil.move(filename, newName)
    print(newName)

def renameBatch(ui, num):
    prefix = getPrefix(ui)
    for file in getLatestFiles(ui, num):
        addPrefix(ui, file, prefix)
    return prefix

def doRenameBatch(ui, num):
    now = datetime.datetime.now().strftime("%H%M%S")
    try:
        prefix = renameBatch(ui, num)
        if prefix == "":
            ui.plainTextEdit.setPlaceholderText(f"[{now}] MOVED {num} FILES.")
        else:
            ui.plainTextEdit.setPlaceholderText(f"[{now}] ADDED \"{prefix}\" TO {num} FILES.")
        ui.plainTextEdit.clear()
    except Exception as e:
        ui.plainTextEdit.setPlaceholderText(f"ERROR: {e.args[0]}!")
        ui.plainTextEdit.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    mainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    readSettings(ui)
    mainWindow.move(ui.position)
    mainWindow.setFixedSize(mainWindow.width(), mainWindow.height())
    mainWindow.show()
    ui.pushButton_01.clicked.connect(lambda: doRenameBatch(ui, 1))
    ui.pushButton_02.clicked.connect(lambda: doRenameBatch(ui, 2))
    ui.pushButton_03.clicked.connect(lambda: doRenameBatch(ui, 3))
    ui.pushButton_04.clicked.connect(lambda: doRenameBatch(ui, 4))
    ui.pushButton_05.clicked.connect(lambda: doRenameBatch(ui, 5))
    ui.pushButton_06.clicked.connect(lambda: doRenameBatch(ui, 6))
    ui.pushButton_07.clicked.connect(lambda: doRenameBatch(ui, 7))
    ui.pushButton_08.clicked.connect(lambda: doRenameBatch(ui, 8))
    ui.pushButton_09.clicked.connect(lambda: doRenameBatch(ui, 9))
    ui.pushButton_10.clicked.connect(lambda: doRenameBatch(ui, 10))
    ui.pushButton_11.clicked.connect(lambda: doRenameBatch(ui, 11))
    ui.pushButton_12.clicked.connect(lambda: doRenameBatch(ui, 12))
    ui.pushButton_13.clicked.connect(lambda: doRenameBatch(ui, 13))
    ui.pushButton_14.clicked.connect(lambda: doRenameBatch(ui, 14))
    ui.pushButton_15.clicked.connect(lambda: doRenameBatch(ui, 15))
    ui.pushButton_16.clicked.connect(lambda: doRenameBatch(ui, 16))
    ui.pushButton_17.clicked.connect(lambda: doRenameBatch(ui, 17))
    ui.pushButton_18.clicked.connect(lambda: doRenameBatch(ui, 18))
    sys.exit(app.exec_())
