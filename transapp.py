import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Translation APP")

        layout = QVBoxLayout()
        self.input = QTextEdit()
        layout.addWidget(self.input)

        button = QPushButton("En-->Ch")
        button.clicked.connect(self.translate)
        layout.addWidget(button)

        self.output = QTextBrowser()
        layout.addWidget(self.output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        tokenizer = AutoTokenizer.from_pretrained("./models/opus-mt-en-zh")
        model = AutoModelForSeq2SeqLM.from_pretrained("./models/opus-mt-en-zh")
        self.translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)

    def translate(self):
        text = self.input.toPlainText()
        t_text = self.translation(text)[0]['translation_text']
        self.output.setText(t_text)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()