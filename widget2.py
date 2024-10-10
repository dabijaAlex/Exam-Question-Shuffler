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

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy, QSpacerItem
from PySide6.QtCore import Qt

from MesBox import MesBox
from exam import Create_All_files
from row import row

#color buttin individually

class Widget2(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.title = 'Application'
        self.parent = parent
        self.resize(500, 500)
        self.layout_set = []

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        return_button = QPushButton("Done")
        return_button.clicked.connect(self.parent.switch_screen)
        return_button.setStyleSheet("background-color: #888;")

        self.layout.addWidget(return_button)


        layout_h = QHBoxLayout()
        Add_button = QPushButton("Add input doc")
        Add_button.clicked.connect(self.add_row)
        Add_button.setStyleSheet("background-color: #888;")
        Add_button.setFixedSize(200,22)


        self.nr_input_files = 0
        self.Nr_label = QLabel(f"Nr of input files = {self.nr_input_files}", self)
        self.Nr_label.setStyleSheet("background-color: #888;")
        self.Nr_label.setMinimumHeight(22)
        self.Nr_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        layout_h.addWidget(Add_button)
        layout_h.addWidget(self.Nr_label)



        self.layout.addLayout(layout_h)

        self.layout.setAlignment(Qt.AlignTop)

        spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout.addItem(spacer)

        self.setLayout(self.layout)


    def add_row(self):
        x = row(self)
        self.layout.addLayout(x)
        ok = x.openFolderDialog_Input2()

        if ok == False:
            x.tip = 2
            x.delete_row()
            self.nr_input_files += 1

        self.nr_input_files += 1
        self.Nr_label.setText(f"Nr of input files = {self.nr_input_files}")


    def create_words(self):
        success = Create_All_files.exec_all(self.folder_path, self.input_file)
        mes_box = MesBox()
        mes_box.display(success, self)