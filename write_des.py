from PyQt5.QtWidgets import QDialog, QLabel, QComboBox
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore, QtGui, QtWidgets
import globals, sqlite3
with sqlite3.connect('pingpong.db') as db:
    cur = db.cursor()


class Writer(QDialog):
    def setupui(self, Form):
        self.setFixedSize(400, 200)
        self.setWindowTitle('Запись')

        self.main_sign = QLabel(self)
        self.main_sign.setFixedSize(300, 30)
        self.main_sign.move(100, 10)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(16)
        font.setBold(True)
        self.main_sign.setFont(font)
        self.main_sign.setText('Выбрать турнир:')

        self.sign_n = QLabel(self)
        self.sign_n.setFixedSize(400, 30)
        self.sign_n.move(24, 106)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(8)
        font.setItalic(True)
        font.setBold(False)
        self.sign_n.setFont(font)
        self.sign_n.setText('   *пользователь может участвовать лишь в тех турнирах, \nпараметры которых'
                            ' соответствуеют его '
                            'секции и категории!')

        self.okay = QtWidgets.QPushButton(self)
        self.okay.setGeometry(QtCore.QRect(45, 150, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.okay.setFont(font)
        self.okay.setStyleSheet("QPushButton {\n"
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
        self.okay.setObjectName("okay")
        self.okay.setText('Выбрать')
        self.okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.can = QtWidgets.QPushButton(self)
        self.can.setGeometry(QtCore.QRect(200, 150, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.can.setFont(font)
        self.can.setStyleSheet("QPushButton {\n"
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
        self.can.setObjectName("can")
        self.can.setText('Отмена')
        self.can.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.spin = QComboBox(self)
        if globals.age_db >= 5 and globals.age_db <= 13:
            cur.execute(f'SELECT Дата FROM info WHERE Секция="{globals.pol_db[0]}" and Категория="5-13"')
        if globals.age_db >= 14 and globals.age_db <= 17:
            cur.execute(f'SELECT Дата FROM info WHERE Секция="{globals.pol_db[0]}" and Категория="14-17"')
        if globals.age_db >= 18 and globals.age_db <= 34:
            cur.execute(f'SELECT Дата FROM info WHERE Секция="{globals.pol_db[0]}" and Категория="18-34"')
        if globals.age_db >= 35 and globals.age_db <= 55:
            cur.execute(f'SELECT Дата FROM info WHERE Секция="{globals.pol_db[0]}" and Категория="35-55"')
        if globals.age_db >= 56 and globals.age_db <= 65:
            cur.execute(f'SELECT Дата FROM info WHERE Секция="{globals.pol_db[0]}" and Категория="56-65"')
        self.dates_list = list()
        for i in cur.fetchall():
            self.dates_list.append(i[0])
        self.spin.addItems(self.dates_list)
        self.spin.setGeometry(45, 55, 305, 40)
        self.spin.setStyleSheet("QComboBox{ \n"
                                "border-width: 2px;\n"
                                "border-color: rgb(148, 148, 148);\n"
                                "border-style: solid;\n"
                                "border-radius: 10px;\n"
                                "}"
                                "QComboBox:hover {\n"
                                "color: #B22222;\n"
                                "}")
        self.prom = list()
        self.spin.activated[str].connect(self.onChanged)

    def onChanged(self, text):
        self.prom.append(text)