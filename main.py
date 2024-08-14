# from PySide6.QtWidgets import QApplication, QWidget

# import sys

# app = QApplication(sys.argv)

# window = QWidget()
# window.show()

# app.exec()

from PySide6.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog, QWidget, QVBoxLayout, QLabel, QPushButton
from widget import Widget
import sys





class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Select Folder Example'
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
        self.button = QPushButton('Select Folder', self)
        self.button.clicked.connect(self.openFolderDialog)
        layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(layout)

        # Variable to store the folder path
        self.folder_path = ""

        self.button2 = QPushButton("Click")
        self.button2.path = "x"
        self.button2.clicked.connect(self.print_path_to_set_folder)
        layout.addWidget(self.button2)


    def print_path_to_set_folder(self):
        print(self.folder_path)


    def openFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly  # Ensure only directories are shown
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if folder:
            self.folder_path = folder
            self.label.setText(f"Selected folder path: {self.folder_path}")
 

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     ex.show()  # Show the main window
#     app.exec()  # Enter the main event loop
#     # print(ex.folder_path)



app = QApplication(sys.argv)

path = []

widget = Widget()
widget.show()


app.exec()

# print(path)












