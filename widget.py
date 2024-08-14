from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QFileDialog, QLabel

from exam import Create_All_files

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Application'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 300, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create a label to show the selected folder path
        self.label = QLabel("Selected folder path will appear here", self)
        layout.addWidget(self.label)

        # Create a button
        self.button = QPushButton('Choose where to place docs', self)
        self.button.clicked.connect(self.openFolderDialog)
        layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(layout)

        # Variable to store the folder path
        self.folder_path = ""
        self.input_file = ""

        self.button2 = QPushButton("Choose input doc")
        self.button2.clicked.connect(self.openFolderDialog_Input)
        layout.addWidget(self.button2)


        self.button3 = QPushButton("Execute")
        self.button3.clicked.connect(self.create_words)
        layout.addWidget(self.button3)




    def print_path_to_set_folder(self):
        print(self.folder_path)


    def openFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if folder:
            self.folder_path = folder
            self.label.setText(f"Selected folder path: {self.folder_path}")


    def openFolderDialog_Input(self):
        # options = QFileDialog.Options()
        # options |= QFileDialog()
        file = QFileDialog.getOpenFileName(self, "Select File", "")
        self.input_file = file

    def create_words(self):
        print("Clicked")
        Create_All_files.exec_all(self.folder_path)
    