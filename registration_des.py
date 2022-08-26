from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


class Ui_reg(object):
    def setupUi(self, Form):
        Form.setObjectName("Регистрация")
        Form.setFixedSize(550, 430)
        Form.setStyleSheet("background-color: white;")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(185, 0, 175, 50))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 220, 240, 40))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "border-width: 1.5px;\n"
                                    "border-color: rgb(148, 148, 148);\n"
                                    "border-style: solid;\n"
                                    "border-radius: 10px;\n"                                 
                                    "}")
        self.lineEdit.setMaxLength(18)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 214, 123, 13))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #FFFFFF;\n"
                                   "color: rgb(148, 148, 148);\n")
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 220, 240, 40))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "border-width: 1.5px;\n"
                                      "border-color: rgb(148, 148, 148);\n"
                                      "border-style: solid;\n"
                                      "border-radius: 10px;\n"                                 
                                      "}")
        self.lineEdit_2.setMaxLength(18)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 214, 150, 13))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: #FFFFFF;\n"
                                   "color: rgb(148, 148, 148);\n")
        self.label_3.setObjectName("label_3")

        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 270, 240, 40))
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
                                      "border-width: 1.5px;\n"
                                      "border-color: rgb(148, 148, 148);\n"
                                      "border-style: solid;\n"
                                      "border-radius: 10px;\n"
                                      "}")
        self.lineEdit_5.setMaxLength(3)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(300, 261, 54, 16))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: #FFFFFF;\n"
                                   "color: rgb(148, 148, 148);\n")
        self.label_6.setObjectName("label_6")

        self.tourn = QtWidgets.QPushButton(Form)
        self.tourn.setGeometry(QtCore.QRect(230, 335, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.tourn.setFont(font)
        self.tourn.setStyleSheet("QPushButton {\n"
                                 " border: 2px;\n"
                                 " border-radius: 10px;\n"
                                 "color: white;\n"
                                 "background: #e45050;\n"
                                 "}"
                                 "QPushButton:hover {\n"
                                 "background: #B22222;\n"
                                 "}"
                                 "QPushButton:pressed {\n"
                                 "background: #800000;\n"
                                 "}")
        self.tourn.setObjectName("pushButton")
        self.tourn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(125, 335, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton {\n"
                                " border: 2px;\n"
                                " border-radius: 10px;\n"
                                "color: white;\n"
                                "background: #A9A9A9;\n"
                                "}"
                                "QPushButton:hover {\n"
                                "background: #808080;\n"
                                "}"
                                "QPushButton:pressed {\n"
                                "background: #696969;\n"
                                "}")
        self.back.setObjectName("pushButton")
        self.back.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.label_error = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_error.setFont(font)
        self.label_error.setText("")
        self.label_error.setStyleSheet("color: #e61919;\n"
                                       "background-color: rgba(0, 0, 0, 0);\n")
        self.label_error.setObjectName("label_error")

        self.photo = QtWidgets.QPushButton(Form)
        self.photo.setGeometry(QtCore.QRect(196, 50, 150, 155))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(75)
        self.photo.setFont(font)
        self.photo.setStyleSheet("QPushButton {\n"
                                 " border: 2px;\n"
                                 " border-radius: 10px;\n"
                                 "color: white;\n"
                                 "background: #e45050;\n"
                                 "}"
                                 "QPushButton:hover {\n"
                                 "background: #E13A3A;\n"
                                 "}"
                                 "QPushButton:pressed {\n"
                                 "background: #B81C1C;\n"
                                 "}")
        self.photo.setObjectName("pushButton")
        self.photo.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.label_2.setText(_translate("Form", " Ввведите ваше имя:"))
        self.label_3.setText(_translate("Form", " Введите вашу фамилию:"))
        self.label_6.setText(_translate("Form", " Возраст:"))
        self.label_error.setText(_translate("Form", ""))
        self.tourn.setText(_translate("Form", "Завершить регистрацию"))
        self.photo.setText(_translate("Form", "+"))
        self.back.setText(_translate("Form", "Отменить"))