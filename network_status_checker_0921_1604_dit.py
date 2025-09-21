# 代码生成时间: 2025-09-21 16:04:28
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon

# 网络连接状态检查器
class NetworkStatusChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # 检查网络连接状态
        self.check_network()

    def initUI(self):
        # 设置窗口标题和图标
        self.setWindowTitle('Network Status Checker')
        self.setWindowIcon(QIcon('network_icon.png'))

        # 创建垂直布局
        self.layout = QVBoxLayout()

        # 创建状态标签
        self.statusLabel = QLabel('Checking network connection...', self)
        self.layout.addWidget(self.statusLabel)

        # 创建检查按钮
        self.checkButton = QPushButton('Check Network', self)
        self.checkButton.clicked.connect(self.check_network)
        self.layout.addWidget(self.checkButton)

        # 设置布局
        self.setLayout(self.layout)
        self.resize(300, 100)

    @pyqtSlot()
    def check_network(self):
        try:
            # 尝试访问网络资源
            response = requests.get('https://www.google.com')

            # 根据响应状态码更新状态标签
            if response.status_code == 200:
                self.statusLabel.setText('Network connected')
                self.statusLabel.setStyleSheet('color: green;')
            else:
                self.statusLabel.setText('Network connection failed')
                self.statusLabel.setStyleSheet('color: red;')
        except requests.RequestException as e:
            # 处理网络请求异常
            QMessageBox.critical(self, 'Network Error', f'Failed to check network connection: {str(e)}')
            self.statusLabel.setText('Network connection failed')
            self.statusLabel.setStyleSheet('color: red;')

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 创建网络连接状态检查器对象
    checker = NetworkStatusChecker()
    checker.show()

    # 启动应用程序事件循环
    sys.exit(app.exec_())