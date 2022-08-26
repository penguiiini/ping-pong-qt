from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QRadioButton, QButtonGroup
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore, QtGui


class Srting(QDialog):
    def setupUi(self, Form):
        Form.setFixedSize(400, 350)
        Form.setWindowTitle('Сортировка')

        self.sign1 = QLabel(self)
        self.sign1.setFixedSize(300, 30)
        self.sign1.move(115, 10)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(14)
        font.setBold(True)
        self.sign1.setFont(font)
        self.sign1.setText('Сортировка по:')

        self.sign2 = QLabel(self)
        self.sign2.setFixedSize(55, 30)
        self.sign2.move(40, 50)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(True)
        self.sign2.setFont(font)
        self.sign2.setText('Полу:')

        self.sign3 = QLabel(self)
        self.sign3.setFixedSize(95, 30)
        self.sign3.move(200, 50)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(True)
        self.sign3.setFont(font)
        self.sign3.setText('Возрасту:')

        self.sign_end = QLabel(self)
        self.sign_end.setFixedSize(300, 50)
        self.sign_end.move(55, 245)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.sign_end.setFont(font)
        self.sign_end.setText('')

        self.sign_error = QLabel(self)
        self.sign_error.setFixedSize(300, 50)
        self.sign_error.move(77, 245)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.sign_error.setFont(font)
        self.sign_error.setStyleSheet("color: #e61919;\n"
                                      "background-color: rgba(0, 0, 0, 0);\n")
        self.sign_error.setText('')

        self.sign_end_age = QLabel(self)
        self.sign_end_age.setFixedSize(200, 50)
        self.sign_end_age.move(175, 254)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.sign_end_age.setFont(font)
        self.sign_end_age.setText('')

        self.radio_age1 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.radio_age1.setFont(font)
        self.radio_age1.setGeometry(QtCore.QRect(195, 85, 150, 30))
        self.radio_age1.setText('5-13')
        self.radio_age1.toggled.connect(self.age1)

        self.button_group_age = QButtonGroup()

        self.radio_age2 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.radio_age2.setFont(font)
        self.radio_age2.setGeometry(QtCore.QRect(195, 115, 150, 30))
        self.radio_age2.setText('14-17')
        self.radio_age2.toggled.connect(self.age2)

        self.radio_age3 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.radio_age3.setFont(font)
        self.radio_age3.setGeometry(QtCore.QRect(195, 145, 150, 30))
        self.radio_age3.setText('18-34')
        self.radio_age3.toggled.connect(self.age3)

        self.radio_age4 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.radio_age4.setFont(font)
        self.radio_age4.setGeometry(QtCore.QRect(195, 175, 150, 30))
        self.radio_age4.setText('35-55')
        self.radio_age4.toggled.connect(self.age4)

        self.radio_age5 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.radio_age5.setFont(font)
        self.radio_age5.setGeometry(QtCore.QRect(195, 205, 150, 30))
        self.radio_age5.setText('56-65')
        self.radio_age5.toggled.connect(self.age5)

        self.button_group_age.addButton(self.radio_age1)
        self.button_group_age.addButton(self.radio_age2)
        self.button_group_age.addButton(self.radio_age3)
        self.button_group_age.addButton(self.radio_age4)
        self.button_group_age.addButton(self.radio_age5)

        self.radio_male = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.radio_male.setFont(font)
        self.radio_male.setGeometry(QtCore.QRect(35, 85, 150, 30))
        self.radio_male.setText('Мужскому')
        self.radio_male.toggled.connect(self.maleselected)
        self.radio_male.toggled.connect(self.maleselected)

        self.button_group_s = QButtonGroup()

        self.radio_female = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setBold(False)
        self.radio_female.setFont(font)
        self.radio_female.setGeometry(QtCore.QRect(35, 115, 150, 30))
        self.radio_female.setText('Женскому')
        self.radio_female.toggled.connect(self.femaleselected)

        self.button_group_s.addButton(self.radio_male)
        self.button_group_s.addButton(self.radio_female)

        self.btn_ok = QPushButton('ОК', self)
        self.btn_ok.setFixedSize(130, 30)
        self.btn_ok.move(65, 305)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet("QPushButton {\n"
                                  "border: 2px;\n"
                                  "border-radius: 10px;\n"
                                  "color: white;\n"
                                  "background: #e45050;\n"
                                  "}"
                                  "QPushButton:hover {\n"
                                  "background: #B22222;\n"
                                  "}"
                                  "QPushButton:pressed {\n"
                                  "background: #800000;\n"
                                  "}")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn_cancel = QPushButton('Отмена', self)
        self.btn_cancel.setFixedSize(130, 30)
        self.btn_cancel.move(205, 305)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
                                      "border: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "color: white;\n"
                                      "background: #e45050;\n"
                                      "}"
                                      "QPushButton:hover {\n"
                                      "background: #B22222;\n"
                                      "}"
                                      "QPushButton:pressed {\n"
                                      "background: #800000;\n"
                                      "}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setCursor(QCursor(QtCore.Qt.PointingHandCursor))