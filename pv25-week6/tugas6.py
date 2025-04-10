from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QColor
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("tugas6.ui", self)

        self.labelNIM = self.findChild(QWidget, "labelNIM")
        self.sliderFontSize = self.findChild(QWidget, "sliderFontSize")
        self.sliderFontColor = self.findChild(QWidget, "sliderFontColor")
        self.sliderBG = self.findChild(QWidget, "sliderBG")

        # Set default NIM
        self.labelNIM.setText("F1D022165")  

        # Hubungkan sinyal slider ke fungsi update
        self.sliderFontSize.valueChanged.connect(self.updateLabelStyle)
        self.sliderFontColor.valueChanged.connect(self.updateLabelStyle)
        self.sliderBG.valueChanged.connect(self.updateLabelStyle)

        self.updateLabelStyle()

    def updateLabelStyle(self):
        font_size = self.sliderFontSize.value()
        font_color_value = self.sliderFontColor.value()
        bg_color_value = self.sliderBG.value()

        font_color = f"rgb({font_color_value}, {font_color_value}, {font_color_value})"
        bg_color = f"rgb({bg_color_value}, {bg_color_value}, {bg_color_value})"

        style = f"""
            QLabel {{
                font-size: {font_size}pt;
                color: {font_color};
                background-color: {bg_color};
            }}
        """
        self.labelNIM.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
