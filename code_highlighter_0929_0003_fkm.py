# 代码生成时间: 2025-09-29 00:03:17
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
import pygments
from pygments.lexers import PythonLexer, HtmlLexer, CssLexer, JavaScriptLexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter, QtFormatter

class CodeHighlighter(QWidget):
    """
    A simple code highlighter using Pygments and PyQt5.
    It can highlight code in various languages.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface.
        """
        self.setWindowTitle('Code Highlighter')
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.text_edit.setLineWrapMode(QTextEdit.NoWrap)
        self.text_edit.setFont(QFont('Consolas', 10))

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def highlight_code(self, language, code):
        """
        Highlight the given code with the specified language.
        """
        try:
            lexer = get_lexer_by_name(language, stripall=True)
            formatter = QtFormatter(get_style_by_name='colorful')
            result = pygments.highlight(code, lexer, formatter)
            self.text_edit.setText(result)
        except Exception as e:
            print(f'Error highlighting code: {e}')

    def set_language(self, language):
        "