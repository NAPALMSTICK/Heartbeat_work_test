# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
app = QApplication([])
win = QWidget()
win.setWindowTitle("Тест Руфье")
win.resize(700,500)
main_vline = QVBoxLayout()
frist_sign = QLabel('Добро пожаловать в программу для определения состояния здоровья')
second_sign = QLabel('''Первым делом лягте на спину, расслабьтесь и сохраняйте такое положение в течение минуты.
Затем измерьте свой пульс в течении 15 сек. Теперь выполните 30 приседаний за 45 секунд и снова измеряйте пкль в течении 15 сек.
Отдохните около 30 секнуд и вновь измеряйте пульс в течении 15 сек.
Запишите данные показатели. ''')
start_btn = QPushButton('Начать')
main_vline.addWidget(frist_sign, alignment = Qt.AlignLeft)
main_vline.addWidget(second_sign, alignment = Qt.AlignLeft)
main_vline.addWidget(start_btn, alignment = Qt.AlignCenter)

win.setLayout(main_vline)
win.show()
app.exec_()