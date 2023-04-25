# FiletSaucer.py

VERSION = "v0.2.0"
DATE = "20230425"

import sys
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 200, 126))
        self.textEdit.setObjectName("textEdit")
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

CONFIG = "FiletSaucer_config.ini"

POSITION_X = 10
POSITION_Y = 200

def readSettings(ui):
    ui.settings = QtCore.QSettings(CONFIG, QtCore.QSettings.IniFormat)
    try:
        position = ui.settings.value("WINDOW/position")
        assert isinstance(position, QtCore.QPoint)
        ui.position = position
    except:
        ui.position = QtCore.QPoint(POSITION_X, POSITION_Y)

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
    sys.exit(app.exec_())
