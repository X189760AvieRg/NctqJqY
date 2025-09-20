# 代码生成时间: 2025-09-20 17:19:57
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QValidator

# 自定义数据验证器类
class CustomValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input, pos):
        # 验证输入，返回(接受状态, 输入字符串, 光标位置)
        if input:
            if input.isdigit():
                return (QValidator.Acceptable, input, pos)
            else:
                return (QValidator.Intermediate, input, pos)
        else:
            return (QValidator.Intermediate, input, pos)

    def fixup(self, text):
        # 返回修正后的字符串
        return text.replace('', '')

# 主窗口类
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和布局
        self.setWindowTitle('Form Validator Example')
        self.setGeometry(100, 100, 300, 100)
        layout = QGridLayout(self)

        # 创建标签和输入框
        self.label = QLabel('Enter a number: ', self)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setValidator(CustomValidator())  # 设置验证器
        self.button = QPushButton('Submit', self)
        self.button.clicked.connect(self.onSubmit)  # 提交按钮事件

        # 添加控件到布局
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.lineEdit, 0, 1)
        layout.addWidget(self.button, 1, 0, 1, 2)

        # 显示窗口
        self.show()

    def onSubmit(self):
        # 提交事件处理
        text = self.lineEdit.text()
        if text.isdigit():
            print('Valid Number:', text)
        else:
            print('Invalid Input!')

# 程序入口点
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()