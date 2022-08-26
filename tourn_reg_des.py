from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QHeaderView, QLabel, QTableView
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QCursor


class Table(object):
    def setupUi(self, Form):
        Form.setFixedSize(900, 510)
        Form.setWindowTitle('Запись на турнир')

        self.write = QLabel(self)
        self.write.setFixedSize(350, 100)
        self.write.move(15, 40)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(14)
        font.setBold(False)
        self.write.setFont(font)
        self.write.setText('Таблица предстоящих турниров:')

        self.sort = QtWidgets.QPushButton(self)
        self.sort.setGeometry(QtCore.QRect(635, 125, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.sort.setFont(font)
        self.sort.setStyleSheet("QPushButton {\n"
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
        self.sort.setObjectName("sort")
        self.sort.setText('Отсортировать по:')
        self.sort.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.writer = QtWidgets.QPushButton(self)
        self.writer.setGeometry(QtCore.QRect(635, 215, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.writer.setFont(font)
        self.writer.setStyleSheet("QPushButton {\n"
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
        self.writer.setObjectName("writer")
        self.writer.setText('Записаться на турнир')
        self.writer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.delete = QtWidgets.QPushButton(self)
        self.delete.setGeometry(QtCore.QRect(635, 305, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.delete.setFont(font)
        self.delete.setStyleSheet("QPushButton {\n"
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
        self.delete.setObjectName("delete")
        self.delete.setText('Отменить участие в турнире')
        self.delete.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.gl = QtWidgets.QPushButton(self)
        self.gl.setGeometry(QtCore.QRect(10, 452, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.gl.setFont(font)
        self.gl.setStyleSheet("QPushButton {\n"
                              "border: 2px;\n"
                              "border-radius: 10px;\n"
                              "color: white;\n"
                              "background: #A9A9A9;\n"
                              "}"
                              "QPushButton:hover {\n"
                              "background: #808080;\n"
                              "}"
                              "QPushButton:pressed {\n"
                              "background: #696969;\n"
                              "}")
        self.gl.setObjectName("gl")
        self.gl.setText('Вернуться на главную страницу')
        self.gl.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.show_all = QtWidgets.QPushButton(self)
        self.show_all.setGeometry(QtCore.QRect(315, 452, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.show_all.setFont(font)
        self.show_all.setStyleSheet("QPushButton {\n"
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
        self.show_all.setObjectName("show_all")
        self.show_all.setText('Показать всю таблицу')
        self.show_all.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.file = QtWidgets.QPushButton(self)
        self.file.setGeometry(QtCore.QRect(635, 395, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.file.setFont(font)
        self.file.setStyleSheet("QPushButton {\n"
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
        self.file.setObjectName("file")
        self.file.setText('Вывести информацию в csv')
        self.file.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.sign = QLabel(self)
        self.sign.setFixedSize(300, 100)
        self.sign.move(285, 0)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(20)
        font.setBold(True)
        self.sign.setFont(font)
        self.sign.setText('Запись на турнир')

        self.create_table()

    def create_table(self):
        self.db1 = QSqlDatabase.addDatabase('QSQLITE')
        self.db1.setDatabaseName("pingpong.db")
        self.db1.open()

        self.view = QTableView(self)
        self.model = QSqlTableModel(self, self.db1)
        self.model.setTable('info')
        self.model.select()

        self.view.setModel(self.model)
        self.view.move(10, 125)
        self.view.setFixedSize(600, 300)

        self.view.setStyleSheet("QHeaderView { \n"
                                "background: #e45050;\n"
                                "}")

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.horizontalHeader().setStretchLastSection(True)
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.view.verticalHeader().setStretchLastSection(True)
        self.view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.view.resizeColumnsToContents()