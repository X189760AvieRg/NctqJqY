# 代码生成时间: 2025-09-22 06:20:23
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt

"""
Test Data Generator using Python and PyQt5 framework.
This program generates a specified number of random test data entries.
"""

class TestDataGenerator(QWidget):
    """
    The main GUI class for the test data generator.
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface.
        """
        self.setWindowTitle('Test Data Generator')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.entries_label = QLabel('Number of entries: ')
        self.entries_input = QLineEdit()
        layout.addWidget(self.entries_label)
        layout.addWidget(self.entries_input)

        self.generate_button = QPushButton('Generate')
        self.generate_button.clicked.connect(self.generate_data)
        layout.addWidget(self.generate_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def generate_data(self):
        """
        Generates random test data based on user input.
        """
        try:
            num_entries = int(self.entries_input.text())
            if num_entries <= 0:
                raise ValueError('Number of entries must be a positive integer.')
            data = self.create_test_data(num_entries)
            self.result_text.setText(data)
        except ValueError as e:
            self.result_text.setText(f'Error: {e}')

    def create_test_data(self, num_entries):
        """
        Creates a specified number of random test data entries.
        """
        test_data = []
        for _ in range(num_entries):
            name = f'Name{random.randint(1, 1000)}'
            age = random.randint(18, 100)
            email = f'{name.lower()}@example.com'
            test_data.append(f'Name: {name}, Age: {age}, Email: {email}
')
        return ''.join(test_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TestDataGenerator()
    window.show()
    sys.exit(app.exec_())