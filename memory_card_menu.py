from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class AddQuestionForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Додати нове питання")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()

        self.layout.setAlignment(Qt.AlignCenter)

        self.question_input = QLineEdit(self)
        self.question_input.setPlaceholderText("Введіть питання")
        self.layout.addWidget(self.question_input)

        self.correct_input = QLineEdit(self)
        self.correct_input.setPlaceholderText("Введіть правильну відповідь")
        self.layout.addWidget(self.correct_input)

        self.wrong1_input = QLineEdit(self)
        self.wrong1_input.setPlaceholderText("Введіть неправильну відповідь")
        self.layout.addWidget(self.wrong1_input)

        self.wrong2_input = QLineEdit(self)
        self.wrong2_input.setPlaceholderText("Введіть неправильну відповідь")
        self.layout.addWidget(self.wrong2_input)

        self.wrong3_input = QLineEdit(self)
        self.wrong3_input.setPlaceholderText("Введіть неправильну відповідь")
        self.layout.addWidget(self.wrong3_input)


        self.add_btn = QPushButton("Додати питання")
        self.layout.addWidget(self.add_btn)

        self.setLayout(self.layout)