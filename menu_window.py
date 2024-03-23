from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLineEdit, QGroupBox, QButtonGroup, QPushButton, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout

menu_win = QWidget()
menu_win.resize(400, 300)
menu_win.setWindowTitle("Меню")

lbl_question = QLabel("Введіть запитання:")
lbl_right_ans = QLabel("Введіть запитання:")
lbl_wrong_ans1 = QLabel("Введіть запитання:")
lbl_wrong_ans2 = QLabel("Введіть запитання:")
lbl_wrong_ans3 = QLabel("Введіть запитання:")

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lbl_question)
vl_labels.addWidget(lbl_right_ans)
vl_labels.addWidget(lbl_wrong_ans1)
vl_labels.addWidget(lbl_wrong_ans2)
vl_labels.addWidget(lbl_wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)

btn_add_question = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
btn_back = QPushButton("Назад")

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

vl_main = QVBoxLayout()
vl_main.addLayout(hl_question)
vl_main.addLayout(hl_buttons)
vl_main.addWidget(btn_back)

menu_win.setLayout(vl_main)