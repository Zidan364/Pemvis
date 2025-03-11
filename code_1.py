from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")

        main_layout = QVBoxLayout()

        # Identity Section
        identity_group = QGroupBox("Identitas (vertical box layout)")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : nama_anda"))
        identity_layout.addWidget(QLabel("Nim : nim_anda"))
        identity_layout.addWidget(QLabel("Kelas : kelas_anda"))
        identity_group.setLayout(identity_layout)
        main_layout.addWidget(identity_group)

        # Navigation Section
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)

        # User Registration Section
        reg_group = QGroupBox("User Registration (form layout)")
        reg_layout = QVBoxLayout()

        reg_layout.addWidget(QLabel("Full Name:"))
        self.name_input = QLineEdit()
        reg_layout.addWidget(self.name_input)

        reg_layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        reg_layout.addWidget(self.email_input)

        reg_layout.addWidget(QLabel("Phone:"))
        self.phone_input = QLineEdit()
        reg_layout.addWidget(self.phone_input)

        reg_layout.addWidget(QLabel("Gender:"))
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        reg_layout.addLayout(gender_layout)

        reg_layout.addWidget(QLabel("Country:"))
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select", "USA", "Canada", "UK", "Indonesia"])
        reg_layout.addWidget(self.country_combo)

        reg_group.setLayout(reg_layout)
        main_layout.addWidget(reg_group)

        # Actions Section
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton("Submit"))
        action_layout.addWidget(QPushButton("Cancel"))
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())