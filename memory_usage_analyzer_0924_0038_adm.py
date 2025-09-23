# 代码生成时间: 2025-09-24 00:38:54
import psutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt

"""
Memory Usage Analyzer using Python and PyQt5.
This program displays the memory usage of the system and provides a simple interface to view the details.
"""

class MemoryUsageAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Memory Usage Analyzer')
        self.setGeometry(100, 100, 600, 400)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Memory usage label
        self.mem_usage_label = QLabel('System Memory Usage: 0%')
        layout.addWidget(self.mem_usage_label)

        # Memory usage details text edit
        self.mem_details = QTextEdit()
        self.mem_details.setReadOnly(True)
        layout.addWidget(self.mem_details)

        # Refresh button
        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.update_memory_usage)
        layout.addWidget(self.refresh_button)

    def update_memory_usage(self):
        try:
            # Get system memory usage
            mem = psutil.virtual_memory()
            mem_usage = mem.percent

            # Update memory usage label
            self.mem_usage_label.setText(f'System Memory Usage: {mem_usage}%')

            # Update memory usage details
            details = f"Total Memory: {mem.total / (1024.0 ** 3):.2f} GB
" \
                     f"Available Memory: {mem.available / (1024.0 ** 3):.2f} GB
" \
                     f"Used Memory: {mem.used / (1024.0 ** 3):.2f} GB
" \
                     f"Memory Usage: {mem.percent}%
" \
                     f"Free Memory: {mem.free / (1024.0 ** 3):.2f} GB
" \
                     f"Active Memory: {mem.active / (1024.0 ** 3):.2f} GB
" \
                     f"Inactive Memory: {mem.inactive / (1024.0 ** 3):.2f} GB"

            self.mem_details.setText(details)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to update memory usage: {e}')

def main():
    app = QApplication(sys.argv)
    analyzer = MemoryUsageAnalyzer()
    analyzer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()