from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGroupBox, QButtonGroup, QPushButton, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout

win = QWidget()
win.resize(400, 300)
win.setWindowTitle("Memory Card")

btn_menu = QPushButton("Меню")

rb_ans1 = QRadioButton()
rb_ans2 = QRadioButton()
rb_ans3 = QRadioButton()
rb_ans4 = QRadioButton()

group = QButtonGroup()
group.addButton(rb_ans1)
group.addButton(rb_ans2)
group.addButton(rb_ans3)
group.addButton(rb_ans4)

lb_question = QLabel("Запитання")
lb_result = QLabel()
lb_right_result = QLabel("Правильна відповідь")

gb_question = QGroupBox("Варіанти відповідей")
rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)

rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

gb_question.setLayout(rb_h1)

gb_answer = QGroupBox()
v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_result)
gb_answer.setLayout(v1)

btn_answer = QPushButton("Відповісти")

v_main = QVBoxLayout()
v_main.addWidget(btn_menu)
v_main.addWidget(lb_question, alignment=Qt.AlignCenter)
v_main.addWidget(gb_question)
v_main.addWidget(gb_answer)
gb_answer.hide()
v_main.addWidget(btn_answer)

win.setLayout(v_main)

win.show()    