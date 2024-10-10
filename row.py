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

from PySide6.QtWidgets import QPushButton, QFileDialog, QLabel, QHBoxLayout, QSizePolicy, QSpacerItem, QLineEdit
from PySide6.QtGui import QIntValidator

from MesBox import MesBox
from exam import Create_All_files
import storage



class row(QHBoxLayout):
    def __init__(self, parent):
        super().__init__()

        self.path = ""
        self.parinte = parent

        self.button_label = QLabel("None", parent)
        self.button_label.setStyleSheet("background-color: #888;")
        self.button_label.setMinimumHeight(20)
        self.button_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button_label.input_file = ""

        self.change_button = QPushButton("Change File")
        self.change_button.clicked.connect(self.change) #please put a file that is not already in use
        self.change_button.setStyleSheet("background-color: #888;")

        self.tip = 1

        self.del_button = QPushButton("Delete FIle")
        self.del_button.clicked.connect(self.delete_row)
        self.del_button.setStyleSheet("background-color: #888;")


        self.box = QLineEdit()
        self.box.textChanged.connect(self.print_text)
        self.box.setMinimumWidth(40)
        self.box.setMaximumWidth(40)
        self.box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.box.setStyleSheet("background-color: #888;")

        int_validator = QIntValidator(0, 200)
        self.box.setValidator(int_validator)


        self.box_label = QLabel(" Nr intrebari per input = ", parent)
        self.box_label.setStyleSheet("background-color: #888;")
        self.box_label.setMinimumHeight(20)
        self.box_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
        



        self.addWidget(self.change_button)
        self.addWidget(self.del_button)
        self.addWidget(self.button_label)

        self.addItem(spacer)

        self.addWidget(self.box_label)
        self.addWidget(self.box)

        self.input_file = ""


    def print_text(self):
        storage.change_number(self.box.text(), self.input_file)



    def delete_row(self):
        self.button_label.deleteLater()
        self.del_button.deleteLater()
        self.change_button.deleteLater()
        self.box.deleteLater()
        self.box_label.deleteLater()
        self.deleteLater()
        if self.tip == 1 :
            self.parinte.nr_input_files -= 1
        self.parinte.Nr_label.setText(f" Nr of input files = {self.parinte.nr_input_files} ")

        storage.remove_from_input_list(self.input_file)


    def openFolderDialog_Input2(self):
        file = QFileDialog.getOpenFileName(self.parinte, "Select File", "")
        if file[0] == "":
            return False

        if storage.is_alr_in_list(file[0]):
            return False
        
        storage.append_to_input_list(file[0])

        self.input_file = file[0]
        self.button_label.setText(f"path =  {self.input_file}")
        return True
    

    def change(self):
        file = QFileDialog.getOpenFileName(self.parinte, "Select File", "")

        if file[0] == "":
            return

        if storage.is_alr_in_list(file[0]):
            return
        
        pos = storage.get_pos(self.input_file)
        storage.input_list[pos] = file[0]
        self.input_file = file[0]
        self.button_label.setText(f" path =  {self.input_file} ")
        return

    def create_words(self):
        success = Create_All_files.exec_all(self.folder_path, self.input_file)
        mes_box = MesBox()
        mes_box.display(success, self)

        