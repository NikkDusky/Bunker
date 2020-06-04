from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(384, 89)
        Dialog.setStyleSheet("background-color: #0b132b;")
        Dialog.setSizeGripEnabled(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.pushButton.setStyleSheet("background-color: #1c2541;\n"
"font: 10pt \"Consolas\";\n"
"color: #6fffe9;")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 10, 113, 31))
        self.lineEdit.setStyleSheet("color: #6fffe9;\n"
"font: 10pt \"Consolas\";\n"
"background-color: #1c2541;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 55, 341, 16))
        self.label.setStyleSheet("color: #6fffe9;\n"
"font: 10pt \"Consolas\";")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Бункер"))
        self.pushButton.setText(_translate("Dialog", "Сгенерировать характеристики"))
