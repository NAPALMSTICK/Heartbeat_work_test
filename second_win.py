# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
def timer1():
    timer = QLabel('0:0:15')
    v_line_2.addWidget(timer, alignment = Qt.AlignRight)
def timer2():
    timer2 = QLabel('0:0:60')
    v_line_2.addWidget(timer2, alignment = Qt.AlignRight)

app_2 = QApplication([])
win_2 = QWidget()
win_2.setWindowTitle("Тест Руфье")
win_2.resize(700,500)

name_sign = QLabel('Введите Ф.И.О')
age_sign = QLabel('Полных лет')
first_task_sign = QLabel('Лягте на спину и замерьте пульс на 15 секунд. Нажмите кнопку начать тест чтобы запустить таймер. Результат запишите в перове поле')

name_enter = QLineEdit()
age_enter = QLineEdit()
second_task = QLabel('Отдохните')
data1 = QLineEdit()
data2 = QLineEdit()


v_line_1 = QVBoxLayout()
v_line_2 = QVBoxLayout()
main_h_line = QHBoxLayout()
frist_start_btn = QPushButton('Начать приседания')
second_start_btn = QPushButton('Начать финальный тест.')
send_all_data = QPushButton('Отправить результаты')

v_line_1.addWidget(name_sign, alignment= Qt.AlignLeft)
v_line_1.addWidget(name_enter, alignment= Qt.AlignLeft)
v_line_1.addWidget(age_sign, alignment= Qt.AlignLeft)
v_line_1.addWidget(age_enter, alignment= Qt.AlignLeft)
v_line_1.addWidget(first_task_sign, alignment= Qt.AlignLeft)
v_line_1.addWidget(frist_start_btn, alignment= Qt.AlignLeft)
v_line_1.addWidget(second_task, alignment= Qt.AlignLeft)
v_line_1.addWidget(second_start_btn, alignment= Qt.AlignLeft)
v_line_1.addWidget(data1, alignment= Qt.AlignLeft)
v_line_1.addWidget(data2, alignment= Qt.AlignLeft)
v_line_1.addWidget(send_all_data, alignment= Qt.AlignCenter)

frist_start_btn.clicked.connect(timer1)
second_start_btn.clicked.connect(timer2)

main_h_line.addLayout(v_line_1)
main_h_line.addLayout(v_line_2)
win_2.setLayout(main_h_line)
win_2.show()
app_2.exec_()