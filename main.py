from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

app = QApplication([])

window = QWidget()
window.resize(800, 1000)
window.move(600, 0)
window.setWindowTitle('текст')

hor = QHBoxLayout()
vert = QVBoxLayout()

input = QLineEdit()
input.setText('текст')
input.setReadOnly(True)

button1 = QPushButton('текст')
button2 = QPushButton('текст')
button3 = QPushButton('текст')
button4 = QPushButton('текст')

text1 = QLabel('текст')
text2 = QLabel('текст')

hor.addWidget(button1, alignment=Qt.AlignCenter)
hor.addWidget(button2, alignment=Qt.AlignCenter)
hor.addWidget(button3, alignment=Qt.AlignCenter)
hor.addWidget(button4, alignment=Qt.AlignCenter)
vert.addWidget(input, alignment=Qt.AlignTop)
vert.addLayout(hor)
vert.addWidget(text1, alignment=Qt.AlignCenter)
vert.addWidget(text2, alignment=Qt.AlignCenter)

window.setLayout(vert)
window.show()
app.exec_()
