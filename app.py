from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox
from autorization_des import Ui_autorization as aut
from tourn_reg_des import Table as table
from registration_des import Ui_reg as reg
from sorting_des import Srting as srt_design
from write_des import Writer as wr_des
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt
from PyQt5 import QtCore
import sys, globals, sqlite3, csv
from message_boxes import open_inf

with sqlite3.connect('pingpong.db') as db:
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(phone TEXT, password TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS chars(username TEXT, familia TEXT, pol TEXT, age INT)""")
    db.commit()


class Autor(QMainWindow, aut):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_inf.clicked.connect(open_inf)
        self.btn_tuda.clicked.connect(self.do_anim)
        self.btn_obr.clicked.connect(self.do_anim1)
        self.push_reg.clicked.connect(self.open_registration)
        self.push_aut.hide()
        self.push_aut.clicked.connect(self.open_registration)
        self.anim1 = QPropertyAnimation(self.frame, b"geometry")
        self.anim = QPropertyAnimation(self.frame, b"geometry")

    def do_anim(self):
        self.anim.setDuration(850)
        self.anim.setStartValue(QRect(90, 230, 120, 30))
        self.anim.setEndValue(QRect(210, 230, 120, 30))
        self.anim.setEasingCurve(QEasingCurve.OutQuint)
        self.anim.start()
        self.frame.setText('  Авторизация')
        self.btn_obr.setText('Регистрация')
        self.push_reg.hide()
        self.push_aut.show()
        self.error_aut.clear()
        self.error_down.clear()

    def do_anim1(self):
        self.anim1.setDuration(850)
        self.anim1.setStartValue(QRect(210, 230, 120, 30))
        self.anim1.setEndValue(QRect(90, 230, 120, 30))
        self.anim1.setEasingCurve(QEasingCurve.OutQuint)
        self.anim1.start()
        self.frame.setText('  Регистрация')
        self.btn_tuda.setText('Авторизация')
        self.push_aut.hide()
        self.push_reg.show()
        self.error_aut.clear()
        self.error_down.clear()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.CTRL + Qt.ShiftModifier):
            if event.key() == Qt.Key_E:
                self.open_registration()

    def open_registration(self):
        self.error_down.setGeometry(90, 473, 400, 40)
        phone, ps, flag = self.lineEdit_p.text().strip(), self.lineEdit_ps.text().strip(), True
        dict_1, current_error, vivod = {'телефон': phone, 'пароль': ps}, '', ''
        for i in dict_1.keys():
            if dict_1[i] == '':
                current_error = i + ' не введен!'
                flag = False
                break
            if i == 'телефон':
                if phone.isdigit() is True:
                    if len(str(phone)) == 11:
                        if str(phone)[0] != '8':
                            current_error = 'первый символ телефона - "8"!'
                            flag = False
                            break
                    else:
                        current_error = 'длина телефона - 11 символов!'
                        flag = False
                        break
                else:
                    current_error = 'телефон - набор чисел!'
                    flag = False
                    break
            elif i == 'пароль':
                if len(ps) < 5:
                    current_error = 'пароль слишком короткий!'
                    flag = False
                    break
            else:
                self.error_aut.setText('')

        if flag is False:
            if current_error == 'телефон не введен!':
                vivod = '        ' + current_error
            elif current_error == 'пароль не введен!':
                vivod = '          ' + current_error
            elif current_error == 'длина телефона - 11 символов!':
                vivod = '' \
                        '' + current_error
            elif current_error == 'пароль слишком короткий!':
                vivod = '   ' + current_error
            elif current_error == 'телефон - набор чисел!':
                vivod = '     ' + current_error
            elif current_error == 'первый символ телефона - "8"!':
                vivod = '' + current_error
            self.error_aut.setText('Неверный формат ввода:')
            self.error_down.setText(vivod)
        else:
            globals.phone_db = phone
            globals.passw_db = ps

            if self.push_aut.isHidden():
                cur.execute(f'SELECT phone FROM users WHERE phone="{globals.phone_db}"')
                if cur.fetchone() is None:
                    cur.execute(f'INSERT INTO users (phone, password) VALUES("{globals.phone_db}",'
                                f' "{globals.passw_db}")')
                    db.commit()
                    self.opening_sec()
                else:
                    self.error_down.setText('     Такая запись уже есть!')

            else:
                cur.execute(f'SELECT password FROM users WHERE phone="{globals.phone_db}"')
                check_passw = cur.fetchall()

                cur.execute(f'SELECT phone FROM users WHERE phone="{globals.phone_db}"')
                check_phone = cur.fetchall()

                try:
                    check_phone[0][0] == globals.phone_db
                except IndexError:
                    self.error_down.setGeometry(14, 467, 400, 40)
                    self.error_aut.setText('')
                    self.error_down.setText('Ошибка авторизации: введены неверные данные!')
                else:
                    if check_passw[0][0] == globals.passw_db:
                        cur.execute(f'SELECT age, pol FROM chars JOIN users ON chars.ROWID = '
                                    f'users.ROWID AND phone="{globals.phone_db}"')
                        p = cur.fetchall()[0]
                        globals.age_db, globals.pol_db = p[0], p[1]
                        self.opening_third()
                    else:
                        self.error_down.setGeometry(19, 467, 400, 40)
                        self.error_aut.setText('')
                        self.error_down.setText('Ошибка авторизации: введен неверный пароль!')

    def opening_third(self):
        self.third_form = Table()
        self.third_form.show()
        self.close()

    def opening_sec(self):
        self.second_form = regis()
        self.second_form.show()
        self.close()


class regis(QMainWindow, reg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tourn.clicked.connect(self.open_tournirs)
        self.back.clicked.connect(self.close_reg)

        self.pol = QComboBox(self)
        self.pol.addItem('Мужской')
        self.pol.addItem('Женский')
        self.pol.setGeometry(20, 270, 240, 40)
        self.pol.setStyleSheet("QComboBox{ \n"
                               "border-width: 2px;\n"
                               "border-color: rgb(148, 148, 148);\n"
                               "border-style: solid;\n"
                               "border-radius: 10px;\n"
                               "}"
                               "QComboBox:hover {\n"
                               "color: #B22222;\n"
                               "}")
        self.pol.activated[str].connect(self.onChanged)

    def onChanged(self, text):
        globals.pol_db = text

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.CTRL + Qt.ShiftModifier):
            if event.key() == Qt.Key_E:
                self.open_tournirs()

    def open_tournirs(self):
        name, familia, age, flag = self.lineEdit.text().strip(), self.lineEdit_2.text().strip(),\
                                   self.lineEdit_5.text().strip(), True
        dicti, current_error = {'имя': name, 'фамилия': familia, 'возраст': age}, ''
        for i in dicti.keys():
            if dicti[i] == '':
                if i == 'имя':
                    current_error = i + ' не введено!'
                if i == 'фамилия':
                    current_error = i + ' не введена!'
                if i == 'возраст':
                    current_error = i + ' не введён!'
                flag = False
                break
            if i == 'возраст':
                if str(age)[0] == '0':
                    current_error = '\nвведенное в графу возраст не должно начинаться с нуля!'
                    flag = False
                    break
                if str(age)[0] != '0' and age.isdigit() is False:
                    current_error = '\nвведенное в графу "возраст" не является числом!'
                    flag = False
                    break
            else:
                self.label_error.setText('')

        if flag is False:
            vivod = 'Неверный формат ввода: ' + current_error
            if current_error == '\nвведенное в графу "возраст" не является числом!':
                vivod = '                     Неверный формат ввода: ' + current_error
                self.label_error.setGeometry(QtCore.QRect(77, 373, 500, 45))
            elif current_error == 'имя не введено!':
                self.label_error.setGeometry(QtCore.QRect(111, 385, 400, 20))
            elif current_error == 'фамилия не введена!':
                self.label_error.setGeometry(QtCore.QRect(90, 385, 400, 20))
            elif current_error == 'возраст не введён!':
                self.label_error.setGeometry(QtCore.QRect(96, 385, 400, 20))
            elif current_error == '\nвведенное в графу возраст не должно начинаться с нуля!':
                vivod = '                           Неверный формат ввода: ' + current_error
                self.label_error.setGeometry(QtCore.QRect(47, 373, 500, 45))
            self.label_error.setText(vivod)
        else:
            if globals.pol_db == '':
                globals.pol_db = 'Мужской'
            globals.name_db = name
            globals.fam_db = familia
            globals.age_db = int(age)
            cur.execute(f'INSERT INTO chars (username, familia, pol, age) VALUES("{globals.name_db}",'
                        f' "{globals.fam_db}", "{globals.pol_db}", "{globals.age_db}")')
            db.commit()
            self.open_third()

    def open_third(self):
        self.third_form = Table()
        self.third_form.show()
        self.close()

    def close_reg(self):
        closing = QMessageBox()
        closing.setStyleSheet("QPushButton {\n"
                              "font-family: SF UI Display; font-size:12px;\n"
                              "color: white;\n"
                              "background: #e45050;\n"
                              "}"
                              "QPushButton:hover {\n"
                              "background: #B22222;\n"
                              "}"
                              "QPushButton:pressed {\n"
                              "background: #800000;\n"
                              "}\n"
                              "QLabel{width: 100px;}")
        closing.setWindowTitle('Внимание!')
        closing.setText('Вы действительно хотите закрыть форму регистрации?')
        closing.setIcon(QMessageBox.Question)
        closing.setInformativeText('Закрытие повлечет несохранение введенных данных')
        closing.addButton("Нет", QMessageBox.NoRole)
        closing.addButton("Да", QMessageBox.YesRole)

        closing.setDefaultButton(QMessageBox.No)
        closing.buttonClicked.connect(self.cl_event)

        closing.exec_()

    def cl_event(self, event):
        if event.text() == 'Да':
            self.back1 = Autor()
            self.back1.show()
            cur.execute(f'DELETE from users WHERE ROWID=(SELECT MAX(rowid) FROM users)')
            db.commit()
            self.close()


class Table(QMainWindow, table):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file.clicked.connect(self.save_2_csv)
        self.sort.clicked.connect(self.sorting)
        self.writer.clicked.connect(self.open_write)
        self.delete.clicked.connect(self.deleter)
        self.gl.clicked.connect(self.to_gl)
        self.show_all.clicked.connect(self.show_all_f)
        self.s = Srting()
        self.w = Writer()

        if globals.y == 1:
            self.model.setTable('info_m_5_13')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 2:
            self.model.setTable('info_m_14_17')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 3:
            self.model.setTable('info_m_18_34')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 4:
            self.model.setTable('info_m_35_55')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 5:
            self.model.setTable('info_m_56_65')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 6:
            self.model.setTable('info_f_5_13')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 7:
            self.model.setTable('info_f_14_17')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 8:
            self.model.setTable('info_f_18_34')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 9:
            self.model.setTable('info_f_35_55')
            self.model.select()
            self.view.setModel(self.model)

        if globals.y == 10:
            self.model.setTable('info_f_55_65')
            self.model.select()
            self.view.setModel(self.model)

    def show_all_f(self):
        self.model.setTable('info')
        self.model.select()
        self.view.setModel(self.model)

    def to_gl(self):
        closing = QMessageBox()
        closing.setStyleSheet("QPushButton {\n"
                              "font-family: SF UI Display; font-size:12px;\n"
                              "color: white;\n"
                              "background: #e45050;\n"
                              "}"
                              "QPushButton:hover {\n"
                              "background: #B22222;\n"
                              "}"
                              "QPushButton:pressed {\n"
                              "background: #800000;\n"
                              "}\n"
                              "QLabel{width: 100px;}")
        closing.setWindowTitle('Внимание!')
        closing.setText('Вы действительно хотите закрыть форму записи?')
        closing.setIcon(QMessageBox.Question)
        closing.addButton("Нет", QMessageBox.NoRole)
        closing.addButton("Да", QMessageBox.YesRole)

        closing.setDefaultButton(QMessageBox.No)
        closing.buttonClicked.connect(self.cl_event)

        closing.exec_()

    def cl_event(self, event):
        if event.text() == 'Да':
            self.back1 = Autor()
            self.back1.show()
            self.close()

    def deleter(self):
        closing = QMessageBox()
        closing.setStyleSheet("QPushButton {\n"
                              "font-family: SF UI Display; font-size:12px;\n"
                              "color: white;\n"
                              "background: #e45050;\n"
                              "}"
                              "QPushButton:hover {\n"
                              "background: #B22222;\n"
                              "}"
                              "QPushButton:pressed {\n"
                              "background: #800000;\n"
                              "}\n"
                              "QLabel{width: 100px;}")
        closing.setWindowTitle('Внимание!')
        closing.setText('Вы действительно хотите отменить запись на турнир?')
        closing.setIcon(QMessageBox.Question)
        closing.addButton("Нет", QMessageBox.NoRole)
        closing.addButton("Да", QMessageBox.YesRole)

        closing.setDefaultButton(QMessageBox.No)
        closing.buttonClicked.connect(self.cl_event_2)

        closing.exec_()

    def cl_event_2(self, event):
        if event.text() == 'Да':
            cur.execute(f'UPDATE users SET userdata = NULL WHERE phone = "{globals.phone_db}"')
            db.commit()

    def open_write(self):
        self.w.show()

    def sorting(self):
        self.s.show()
        self.close()

    def save_2_csv(self):
        with open('results.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)


class Writer(wr_des):
    def __init__(self):
        super().__init__()
        self.setupui(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.can.clicked.connect(self.cancel)
        self.okay.clicked.connect(self.oky)

    def cancel(self):
        self.close()

    def oky(self):
        if len(self.prom) != 0:
            globals.date = self.prom[-1]
        else:
            globals.date = self.dates_list[0]
        cur.execute(f'UPDATE users SET userdata = "{globals.date}" WHERE phone = "{globals.phone_db}"')
        db.commit()
        self.close()


class Srting(srt_design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_ok.clicked.connect(self.checking)

    def checking(self):
        if self.sign_end.text() == '        Выбранная сортировка:\nмужской пол,':
            if self.sign_end_age.text() == 'возраст - 5-13 лет':
                globals.y = 1
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 14-17 лет':
                globals.y = 2
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 18-34 лет':
                globals.y = 3
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 35-55 лет':
                globals.y = 4
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 56-65 лет':
                globals.y = 5
                self.opening_table()

        elif self.sign_end.text() == '        Выбранная сортировка:\nженский пол,':
            if self.sign_end_age.text() == 'возраст - 5-13 лет':
                globals.y = 6
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 14-17 лет':
                globals.y = 7
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 18-34 лет':
                globals.y = 8
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 35-55 лет':
                globals.y = 9
                self.opening_table()

            if self.sign_end_age.text() == 'возраст - 56-65 лет':
                globals.y = 10
                self.opening_table()

        elif self.sign_end.text() == '' and self.sign_end_age.text() == '':
            self.sign_error.setText('Ошибка: ничего не введено!')

    def opening_table(self):
        self.t = Table()
        self.t.show()
        self.close()

    def cancel(self):
        self.t = Table()
        self.t.show()
        self.close()

    def maleselected(self, selected):
        if selected:
            self.sign_error.setText('')
            self.sign_end.setText('        Выбранная сортировка:\nмужской пол,')

    def femaleselected(self, selected):
        if selected:
            self.sign_error.setText('')
            self.sign_end.setText('        Выбранная сортировка:\nженский пол,')

    def age1(self, selected):
        if selected:
            self.sign_error.setText('')
            self.sign_end_age.setText('возраст - 5-13 лет')

    def age2(self, selected):
        if selected:
            self.sign_error.setText('')
            self.sign_end_age.setText('возраст - 14-17 лет')

    def age3(self, selected):
        if selected:
            self.sign_error.setText('')
            self.sign_end_age.setText('возраст - 18-34 лет')

    def age4(self, selected):
        if selected:
            self.sign_error.setText('')
            self.sign_end_age.setText('возраст - 35-55 лет')

    def age5(self, selected):
        if selected:
            self.sign_error.setText('')
            self.sign_end_age.setText('возраст - 56-65 лет')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Autor()
    ex.show()
    sys.exit(app.exec_())