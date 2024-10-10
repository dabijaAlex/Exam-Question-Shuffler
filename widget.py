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

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QSizePolicy, QHBoxLayout,  QSpacerItem, QCheckBox, QLineEdit, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator

from MesBox import MesBox
from exam import Create_All_files
import storage
from validator import FloatValidator
# from widget2 import Widget2


#color buttin individually

class Widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.title = 'Application'
        self.resize(500, 500)
        self.parent = parent
        # self.font
        self.bold = False
        self.font_size_pct = 8 
        self.font_name = "Calibri"
        self.header_path = ""
        self.folder_path = ""
        self.input_file = ""
        self.nr_subiecte = 0

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        h_layout_path_to_folder = QHBoxLayout()



        path_to_folder_button = QPushButton('Choose where to place docs', self)
        path_to_folder_button.clicked.connect(self.openFolderDialog)
        path_to_folder_button.setStyleSheet("background-color: #888;")
        path_to_folder_button.setMinimumWidth(200)
        h_layout_path_to_folder.addWidget(path_to_folder_button)

        self.label_path = QLabel(" Selected folder path will appear here ", self)
        self.label_path.setStyleSheet("background-color: #888;")
        self.label_path.setMinimumHeight(20)
        self.label_path.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        h_layout_path_to_folder.addWidget(self.label_path)

        layout.addLayout(h_layout_path_to_folder)



        header_layout = QHBoxLayout()

        header_button = QPushButton("Choose header doc")
        header_button.clicked.connect(self.openFolderDialog_header_doc)
        header_button.setStyleSheet("background-color: #888;")
        header_button.setMinimumWidth(200)
        header_layout.addWidget(header_button)

        self.label_header_doc = QLabel(" Selected header doc path will appear here ", self)
        self.label_header_doc.setStyleSheet("background-color: #888;")
        self.label_header_doc.setMinimumHeight(20)
        self.label_header_doc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header_layout.addWidget(self.label_header_doc)

        layout.addLayout(header_layout)


        spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout.addItem(spacer)


        input_button = QPushButton("Choose input doc")
        input_button.clicked.connect(self.the_window)
        input_button.setStyleSheet("background-color: #888;")
        layout.addWidget(input_button)


        font_row = QHBoxLayout()


        bold = QCheckBox("Bold")
        bold.toggled.connect(self.bold_toggled)
        bold.setStyleSheet("background-color: #888;")
        bold.setMinimumHeight(20)
        bold.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        font_size_label = QLabel("Write font size (.0 or .5) : ", self)
        font_size_label.setStyleSheet("background-color: #888;")
        font_size_label.setMinimumHeight(20)
        font_size_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        self.font_size_box = QLineEdit()
        self.font_size_box.textChanged.connect(self.font_size)
        self.font_size_box.setStyleSheet("background-color: #888;")
        self.font_size_box.setMaximumHeight(20)
        self.font_size_box.setMaximumWidth(40)
        self.font_size_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        float_validator = FloatValidator()
        self.font_size_box.setValidator(float_validator)


        self.dropdown_names = QComboBox()
        self.dropdown_names.addItem("Arial")
        self.dropdown_names.addItem("Times New Roman")
        self.dropdown_names.addItem("Calibri")
        self.dropdown_names.addItem("Verdana")
        self.dropdown_names.addItem("Tahoma")
        self.dropdown_names.addItem("Georgia")
        self.dropdown_names.addItem("Courier New")
        self.dropdown_names.addItem("Comic Sans MS")
        self.dropdown_names.addItem("Trebuchet MS")
        self.dropdown_names.addItem("Lucida Console")
        self.dropdown_names.addItem("Impact")
        self.dropdown_names.addItem("Palatino Linotype")
        self.dropdown_names.addItem("Garamond")
        self.dropdown_names.addItem("Bookman Old Style")
        self.dropdown_names.addItem("Century Gothic")
        self.dropdown_names.addItem("Franklin Gothic Medium")
        self.dropdown_names.addItem("Gill Sans MT")
        self.dropdown_names.addItem("Lucida Sans Unicode")
        self.dropdown_names.addItem("Arial Black")
        self.dropdown_names.addItem("Tahoma")
        self.dropdown_names.addItem("Symbol")
        self.dropdown_names.addItem("Wingdings")
        self.dropdown_names.addItem("Cambria")
        self.dropdown_names.addItem("Constantia")
        self.dropdown_names.addItem("Corbel")
        self.dropdown_names.addItem("Candara")
        self.dropdown_names.addItem("Rockwell")
        self.dropdown_names.addItem("Segoe UI")
        self.dropdown_names.addItem("Open Sans")
        self.dropdown_names.addItem("Roboto")

        self.dropdown_names.currentIndexChanged.connect(self.name)
        self.dropdown_names.setStyleSheet("background-color: #888;")
        self.dropdown_names.setMaximumHeight(20)
        self.dropdown_names.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        spacer = QSpacerItem(50, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)

        font_row.setAlignment(Qt.AlignLeft)





        font_row.addWidget(bold)
        font_row.addItem(spacer)

        font_row.addWidget(font_size_label)
        font_row.addWidget(self.font_size_box)

        font_row.addItem(spacer)
        font_row.addWidget(self.dropdown_names)

        layout.addLayout(font_row)



        spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addItem(spacer)


        nr_sub_row = QHBoxLayout()

        nr_subiecte_label = QLabel("How many tests? : ", self)
        nr_subiecte_label.setStyleSheet("background-color: #888;")
        nr_subiecte_label.setMinimumHeight(20)
        nr_subiecte_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        self.nr_subiecte_label_box = QLineEdit()
        self.nr_subiecte_label_box.textChanged.connect(self.get_nr_subiecte)
        self.nr_subiecte_label_box.setStyleSheet("background-color: #888;")
        self.nr_subiecte_label_box.setMaximumHeight(20)
        self.nr_subiecte_label_box.setMaximumWidth(40)
        self.nr_subiecte_label_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        int_validator = QIntValidator(0, 1000)
        self.nr_subiecte_label_box.setValidator(int_validator)

        nr_sub_row.addWidget(nr_subiecte_label)
        nr_sub_row.addWidget(self.nr_subiecte_label_box)

        nr_sub_row.setAlignment(Qt.AlignLeft)

        layout.addLayout(nr_sub_row)





        spacer = QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addItem(spacer)


        execute_button = QPushButton("Execute")
        execute_button.clicked.connect(self.create_words)
        execute_button.setStyleSheet("background-color: #888;")
        layout.addWidget(execute_button)


        layout.setAlignment(Qt.AlignTop)

        self.setLayout(layout)


    def get_nr_subiecte(self):
        self.nr_subiecte = int(self.nr_subiecte_label_box.text())



    def name(self):
        self.font_name = self.dropdown_names.currentText()


    def font_size(self):
        x = self.font_size_box.text()
        if x != "":
            x = float(x)
        else:
            x = float(8)

        self.font_size_pct = x


    def bold_toggled(self, checked):
        if (checked):
            self.bold = True
        else:
            self.bold = False


    def the_window(self):
        self.parent.switch_screen()


    def openFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if folder:
            self.folder_path = folder
            self.label_path.setText(f"Selected folder path: {self.folder_path}")

    def openFolderDialog_header_doc(self):
        header = QFileDialog.getOpenFileName(self, "Select Folder", "")
        if header:
            self.header_path = header[0]
            self.label_header_doc.setText(f"Selected header doc path: {self.header_path}")


    def create_words(self):
        success = Create_All_files.exec_all(self.folder_path, storage.input_list, storage.input_list_numbers, self.header_path,
                                            self.bold, self.font_size_pct, self.font_name, self.nr_subiecte)
        mes_box = MesBox()
        mes_box.display(success, self)