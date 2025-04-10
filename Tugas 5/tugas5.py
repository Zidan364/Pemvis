import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QPushButton


class FormValidation(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Tugas5.ui", self)

        # Ambil field dari UI
        self.nameField = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.emailField = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.ageField = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")
        self.phoneField = self.findChild(QtWidgets.QLineEdit, "lineEdit_4")
        self.addressField = self.findChild(QtWidgets.QLineEdit, "lineEdit_5")
        self.genderBox = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.educationBox = self.findChild(QtWidgets.QComboBox, "comboBox_2")

        # Tambahkan tombol Save
        self.saveButton = QPushButton("Save", self)
        self.saveButton.setGeometry(120, 310, 75, 23)
        self.saveButton.clicked.connect(self.saveForm)

        # Tambahkan tombol Clear
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setGeometry(220, 310, 75, 23)
        self.clearButton.clicked.connect(self.clearForm)

    def saveForm(self):
        # Cek jika ada field kosong
        if (
            not self.nameField.text().strip()
            or not self.emailField.text().strip()
            or not self.ageField.text().strip()
            or not self.phoneField.text().strip()
            or not self.addressField.text().strip()
            or self.genderBox.currentText().strip() == ""
            or self.educationBox.currentText().strip() == ""
        ):
            QMessageBox.warning(self, "Warning", "All fields are required.")
        else:
            QMessageBox.information(self, "Success", "Form saved successfully!")

    def clearForm(self):
        self.nameField.clear()
        self.emailField.clear()
        self.ageField.clear()
        self.phoneField.clear()
        self.addressField.clear()
        self.genderBox.setCurrentIndex(0)
        self.educationBox.setCurrentIndex(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormValidation()
    window.setWindowTitle("Form Validation")
    window.show()
    sys.exit(app.exec())
