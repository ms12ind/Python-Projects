from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from openai import ChatCompletion, ChatCompletionType
import os

class ChatBotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot")
        self.setGeometry(100, 100, 400, 500)

        layout = QVBoxLayout()

        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        self.text_input = QTextEdit()
        layout.addWidget(self.text_input)

        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def send_message(self):
        message = self.text_input.toPlainText()
        self.text_display.append("You: " + message)
        response = self.get_bot_response(message)
        self.text_display.append("Bot: " + response)
        self.text_input.clear()

    def get_bot_response(self, message):
        openai_chat = ChatCompletion.create(
            model="text-davinci-003",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            max_tokens=50,
            temperature=0.9,
            stop=["\n", "User:", "Bot:"],
            timeout=60,
            logprobs=10,
            completion_type=ChatCompletionType.REGULAR
        )
        return openai_chat.choices[0].message['content']

def main():
    app = QApplication([])
    window = ChatBotGUI()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()