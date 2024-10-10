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

from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget
import sys

from widget import Widget
from widget2 import Widget2


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet("background-color: #222;")
        self.resize(500, 500)


        self.stacked_widget = QStackedWidget()

        self.show()
        self.initUI()

    def initUI(self):

        self.page1 = Widget(self)
        self.page2 = Widget2(self)

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        self.setCentralWidget(self.stacked_widget)


    def switch_screen(self):
        # Get the index of the current page
        current_index = self.stacked_widget.currentIndex()
        # Switch to the next page
        next_index = (current_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(next_index)



app = QApplication(sys.argv)

path = []

widget = MainWindow()
widget.show()


app.exec()    