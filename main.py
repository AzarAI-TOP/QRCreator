'''
Author: AzarAI
Email: 3420396703@qq.com
Date: 2023-04-10 11:03:43
LastEditTime: 2023-04-10 11:54:07
'''
import sys
import pyqrcode
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__(None)

        self.whiteImage = QPixmap(400, 500)
        self.whiteImage.fill(QColor('black'))

        self.template = '<center><img src="data:image/png;base64,{}"></center>'

        self.setUI()

    def setUI(self):
        self.setWindowTitle('AI-QRCreator')
        self.setFixedSize(400, 700)

        # Add Component
        self.text = QPlainTextEdit(self)
        self.label = QLabel(self)

        # Set Component
        self.text.setGeometry(0, 0, 400, 200)
        self.text.textChanged.connect(self.on_change)

        self.label.setGeometry(0, 200, 400, 500)
        self.label.setPixmap(self.whiteImage)


    def on_change(self):
        t = self.text.toPlainText()
        if t:
            qr = pyqrcode.create(t, encoding='utf-8')
            pic = qr.png_as_base64_str(scale=9,quiet_zone=1)
            self.label.setText(self.template.format(pic))
        else:
            self.label.setPixmap(self.whiteImage)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
