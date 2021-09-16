#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys

import execjs
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.js_ide = self.load_json()

        self.pushButton_run.clicked.connect(self.run)

    @staticmethod
    def load_json():
        with open(r'js_uncode.js', 'r', encoding='utf-8') as f:
            js = f.read()
        return execjs.compile(js, cwd=r'./node_modules')

    def run(self):
        text_old = self.textEdit_old.toPlainText().strip()
        if not text_old:
            return
        text_new = self.js_ide.call('uncode', text_old)
        self.textEdit_new.setPlainText(text_new)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
