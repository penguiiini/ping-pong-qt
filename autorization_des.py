from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


class Ui_autorization(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(425, 580)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: white;\n")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(93, 170, 460, 31))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit_p = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_p.setGeometry(QtCore.QRect(70, 300, 281, 40))
        self.lineEdit_p.setStyleSheet("QLineEdit {\n"
                                      "border-width: 1.5px;\n"
                                      "border-color: rgb(148, 148, 148);\n"
                                      "border-style: solid;\n"
                                      "border-radius: 10px;\n"                                 
                                      "}")
        self.lineEdit_p.setMaxLength(11)
        self.lineEdit_p.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_p.setObjectName("lineEdit_p")

        self.push_reg = QtWidgets.QPushButton(Dialog)
        self.push_reg.setGeometry(QtCore.QRect(90, 400, 241, 31))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.push_reg.setFont(font)
        self.push_reg.setStyleSheet("QPushButton {\n"
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
        self.push_reg.setObjectName("push_reg")
        self.push_reg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.push_aut = QtWidgets.QPushButton(Dialog)
        self.push_aut.setGeometry(QtCore.QRect(90, 400, 241, 31))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.push_aut.setFont(font)
        self.push_aut.setStyleSheet("QPushButton {\n"
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
        self.push_aut.setObjectName("push_aut")
        self.push_aut.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.lineEdit_ps = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ps.setGeometry(QtCore.QRect(70, 350, 281, 40))
        self.lineEdit_ps.setStyleSheet("QLineEdit {\n"
                                       "border-width: 1.5px;\n"
                                       "border-color: rgb(148, 148, 148);\n"
                                       "border-style: solid;\n"
                                       "border-radius: 10px;\n"                                 
                                       "}")
        self.lineEdit_ps.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_ps.setMaxLength(22)
        self.lineEdit_ps.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_ps.setObjectName("lineEdit_ps")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(87, 342, 52, 16)) # 45
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: #FFFFFF;\n"
                                   "color: rgb(148, 148, 148);\n")
        self.label_4.setObjectName("label_4")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(87, 292, 94, 16))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: #FFFFFF;\n"
                                   "color: rgb(148, 148, 148);\n")
        self.label_3.setObjectName("label_3")

        self.pushButton_inf = QtWidgets.QPushButton(Dialog)
        self.pushButton_inf.setGeometry(QtCore.QRect(90, 540, 241, 23))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.pushButton_inf.setFont(font)
        self.pushButton_inf.setStyleSheet("QPushButton {\n"
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
        self.pushButton_inf.setObjectName("pushButton_inf")
        self.pushButton_inf.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.label_icon = QtWidgets.QLabel(Dialog)
        self.label_icon.setGeometry(QtCore.QRect(107, 50, 250, 110))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_icon.setFont(font)
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap("icon.jpg"))
        self.label_icon.setObjectName("label_icon")

        self.btn_und = QtWidgets.QPushButton(Dialog)
        self.btn_und.setGeometry(QtCore.QRect(90, 230, 240, 30))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.btn_und.setFont(font)
        self.btn_und.setStyleSheet("QPushButton {\n"
                                   "border-width: 1.5px;\n"
                                   "border: 2px;\n"
                                   "border-radius: 15px;\n"
                                   "background-color: #e8e8e8;\n"
                                   "color: #FFFFFF;\n"
                                   "}")
        self.btn_und.setObjectName("btn_und")

        self.btn_tuda = QtWidgets.QPushButton(Dialog)
        self.btn_tuda.setGeometry(QtCore.QRect(210, 230, 120, 30))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.btn_tuda.setFont(font)
        self.btn_tuda.setStyleSheet("QPushButton {\n"
                                    "border-width: 1.5px;\n"
                                    "border: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "background-color: #e8e8e8;\n"
                                    "color: #FFFFFF;\n"
                                    "}")
        self.btn_tuda.setObjectName("btn_tuda")
        self.btn_tuda.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn_obr = QtWidgets.QPushButton(Dialog)
        self.btn_obr.setGeometry(QtCore.QRect(90, 230, 120, 30))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.btn_obr.setFont(font)
        self.btn_obr.setStyleSheet("QPushButton {\n"
                                   "border-width: 1.5px;\n"
                                   "border: 2px;\n"
                                   "border-radius: 15px;\n"
                                   "background-color: #e8e8e8;\n"
                                   "color: #FFFFFF;\n"
                                   "}")
        self.btn_obr.setObjectName("btn_obr")
        self.btn_obr.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.frame = QtWidgets.QLabel(self)
        self.frame.setGeometry(90, 230, 120, 30)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QLabel {\n"
                                 "border-width: 1.5px;\n"
                                 " border: 2px;\n"
                                 " border-radius: 15px;\n"
                                 "color: white;\n"
                                 "background: #e45050;\n"
                                 "}"
                                 "QPushButton:hover {\n"
                                 "background: #B22222;\n"
                                 "}"
                                 "QPushButton:pressed {\n"
                                 "background: #800000;\n"
                                 "}")
        self.frame.setObjectName("frame")

        self.rast = 110
        self.error_aut = QtWidgets.QLabel(self)
        self.error_aut.setGeometry(self.rast, 453, 400, 40)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.error_aut.setFont(font)
        self.error_aut.setText("")
        self.error_aut.setStyleSheet("color: #e61919;\n"
                                     "background-color: rgba(0, 0, 0, 0);\n")
        self.error_aut.setObjectName("error_aut")

        self.error_down = QtWidgets.QLabel(self)
        self.error_down.setGeometry(90, 473, 400, 40)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.error_down.setFont(font)
        self.error_down.setText("")
        self.error_down.setStyleSheet("color: #e61919;\n"
                                      "background-color: rgba(0, 0, 0, 0);\n")
        self.error_down.setObjectName("error_down")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PP Tournament client"))
        self.label.setText(_translate("Dialog", "PP Tournament"))
        self.label_3.setText(_translate("Dialog", ' Телефон(с "8"):'))
        self.push_aut.setText(_translate("Dialog", "Войти"))
        self.push_reg.setText(_translate("Dialog", "Продолжить регистрацию"))
        self.pushButton_inf.setText(_translate("Dialog", "Информация"))
        self.btn_tuda.setText(_translate("Dialog", "Авторизация"))
        self.frame.setText(_translate("Dialog", "  Регистрация"))
        self.error_aut.setText(_translate("Dialog", ""))
        self.error_down.setText((_translate("Dialog", "")))
        self.label_4.setText(_translate("Dialog", " Пароль:"))