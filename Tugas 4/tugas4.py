# Form implementation generated from reading ui file 'Tugas4.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(513, 319)
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(150, 10, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 41, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(100, 70, 41, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(parent=Form)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 70, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(100, 130, 321, 81))
        self.listWidget.setObjectName("listWidget")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 181, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Bimoli (Rp. 20,000)"))
        self.comboBox.setItemText(1, _translate("Form", "Beras 5 kg (Rp. 75,000)"))
        self.comboBox.setItemText(2, _translate("Form", "Kecap ABC (Rp. 7,000)"))
        self.comboBox.setItemText(3, _translate("Form", "Saos Saset (Rp. 2,500)"))
        self.label.setText(_translate("Form", "Product"))
        self.label_2.setText(_translate("Form", "Quantity"))
        self.label_3.setText(_translate("Form", "Discount"))
        self.comboBox_2.setItemText(0, _translate("Form", "5%"))
        self.comboBox_2.setItemText(1, _translate("Form", "10%"))
        self.comboBox_2.setItemText(2, _translate("Form", "15%"))
        self.pushButton.setText(_translate("Form", "Add to Cart"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.label_4.setText(_translate("Form", "Total :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
