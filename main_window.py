from PyQt5 import QtWidgets, QtCore, QtGui
from tool_details import TOOL_DETAILS
from find_tool_executable import find_tool_executable
from remove_javasoft_key import remove_javasoft_key
from remove_permanent_files import remove_permanent_files
from open_ide import open_ide

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JetBrains IDE Reset")
        self.setGeometry(300, 300, 400, 300)

        self.main_layout = QtWidgets.QVBoxLayout()

        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.group = QtWidgets.QButtonGroup(self)
        self.group.setExclusive(True)

        row = 0
        col = 0
        for i, tool_name in enumerate(TOOL_DETAILS.keys()):
            radio = QtWidgets.QRadioButton(tool_name)
            self.group.addButton(radio)
            self.grid_layout.addWidget(radio, row, col)
            col += 1
            if col == 2:  # Change this value to arrange items in more columns
                col = 0
                row += 1

        self.main_layout.addLayout(self.grid_layout)

        self.reset_button = QtWidgets.QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset)
        self.main_layout.addWidget(self.reset_button, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(self.main_layout)

    def reset(self):
        selected_button = self.group.checkedButton()
        if selected_button:
            selected_tool = selected_button.text()

            # Check if the tool is installed
            tool_keyword, executable_name = TOOL_DETAILS[selected_tool]
            tool_executable = find_tool_executable(tool_keyword, executable_name)
            if not tool_executable:
                QtWidgets.QMessageBox.critical(self, "Error", f"{selected_tool} not found. Please make sure it is installed.")
                return

            results = []

            # Perform the JavaSoft key removal
            success, message = remove_javasoft_key()
            results.append(message)
            if not success:
                QtWidgets.QMessageBox.critical(self, "Error", "\n".join(results))
                return

            # Perform the PermanentUserId and PermanentDeviceId removal
            results.extend(remove_permanent_files())
            for result in results:
                if "Error" in result:
                    QtWidgets.QMessageBox.critical(self, "Error", "\n".join(results))
                    return

            # Attempt to open the IDE
            success, message = open_ide(selected_tool)
            results.append(message)
            if success:
                QtWidgets.QMessageBox.information(self, "Success", "\n".join(results))
                QtCore.QTimer.singleShot(3000, self.close)
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "\n".join(results))
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select an IDE.")