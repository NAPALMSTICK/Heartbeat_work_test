# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

time = QTime(0, 0, 15)
timer = QTimer()
timer.timeout.connect(timerEvent)
timer.start(1000)

app_2 = QApplication([])
win_2 = QWidget()
win_2.setWindowTitle("Тест Руфье")
win_2.resize(700,500)

name_sign = QLabel('Введите Ф.И.О')
age_sign = QLabel('Полных лет')
first_task_sign = QLabel('Лягте на спину и замерьте пульс на 15 секунд. Нажмите кнопку начать тест чтобы запустить таймер. Результат запишите в перове поле')


v_line_1 = QVBoxLayout()
v_line_2 = QVBoxLayout()
main_h_line = QHBoxLayout()
v_line_2.addWidget(timer, alignment = Qt.AlignCenter)

main_h_line.addLayout(v_line_2)
win_2.setLayout(main_h_line)
win_2.show()
app.exec_()