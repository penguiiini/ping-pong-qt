from PyQt5.QtWidgets import QMessageBox


def open_inf():
    inf = QMessageBox()
    inf.setFixedSize(500, 500)
    inf.setStyleSheet("QPushButton {\n"
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
    inf.setWindowTitle('Внимание!')
    inf.setText('Информация о приложении PP Tournament client')
    inf.setIcon(QMessageBox.Question)
    inf.setInformativeText('Привет! "PP Tournament client" '
                           '- это приложение для регистрации на турниры по настольному теннису.'
                           ' Вы можете выбрать между регистрацией, если у Вас еще нет аккаунта, и авторизацией, '
                           'если Вы уже зарегистрированы с помощью кнопки-переключателя "Регистрация-Авторизация."'
                           'Если Вы выберете кнопку "Регистрация", то Вы сможете ввести свои данные для первичной '
                           'регистрации. Дальше, нажав кнопку "Продолжить регистрацию", Вы попадете на окно '
                           'вторичной регистрации, где Вам надо будет ввести дополнительные данные для завершения'
                           ' регистрации. Дальше Вы попадете на окно записи на турнир. Нажав же кнопку '
                           '"Авторизация", Вы должны будете ввести свои данные, которые Вы вводили при'
                           ' регистрации. После нажатия кнопки "Войти" система проверит, правильно ли Вы ввели '
                           'данные и даст Вам доступ к окну записи на турнир, в случае, если данные верны. '
                           'В окне записи на турнир есть несколько кнопок: во-первых, Вы можете отсортировать '
                           'турнирную таблицу и посмотреть те турниры, которые нужны именно Вам. Нажав кнопку '
                           '"Записаться на турнир", Вы сможете записаться на турнир, но Вы можете записаться лишь'
                           ' на те турниры, которые соответсвуют Вашим полу и возрасту, а также где количество '
                           'свободных мест не меньше 1. Помните, что Вы можете записаться лишь на один турнир! '
                           'Также Вы можете отменить '
                           'участие в турнире, нажав соответствующую кнопку "Отменить участие в турнире". '
                           'Горячие клавиши: если Вы нажмете сочетание клавиш "Ctrl" + "Shift" + "E",'
                           ' то активируется кнопка перехода на следующую страницу.')
    inf.addButton("ОК", QMessageBox.YesRole)

    inf.exec_()


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

    closing.exec_()