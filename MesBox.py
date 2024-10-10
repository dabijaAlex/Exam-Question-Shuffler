# Copyright 2024 Dabija Alexandru

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and 
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from PySide6.QtWidgets import QMessageBox, QApplication
from PySide6.QtGui import QIcon

class MesBox(QMessageBox):
    def __init__(self):
        super().__init__()
        

        screen_geometry = QApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        self.setGeometry(screen_width / 2 - (self.width() / 5),screen_height / 2 - self.height() / 5, 100, 100)


    def display(self, success, parent):
        if success == 1:
            self.information_box()
        else:
            self.critical_box()


    def information_box(self):
        self.setWindowIcon(QIcon("info-sign.png"))
        self.setWindowTitle("Success")
        self.setText("The docs have been created")
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Ok)
        self.setDefaultButton(QMessageBox.Ok)
        ret = self.exec()


    def critical_box(self):
        self.setWindowIcon(QIcon("close.png"))
        self.setWindowTitle("Error")
        self.setText("Please provide path to file / folder")
        self.setIcon(QMessageBox.Critical)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Ok)
        

        ret = self.exec()
