import sys
import random
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtCore import Qt, QEvent


class MouseTrackerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mouse Event Handler")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Move the mouse", self)
        self.label.setGeometry(250, 180, 120, 30)
        self.label.setStyleSheet("background-color: lightblue; border: 1px solid black;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Mengaktifkan event filter untuk label
        self.label.installEventFilter(self)

    def mouseMoveEvent(self, event):
        self.label.setText(f"X: {int(event.position().x())}, Y: {int(event.position().y())}")

    def enterEvent(self, event):
        self.setMouseTracking(True)

    def eventFilter(self, source, event):
        if source == self.label and event.type() == QEvent.Type.Enter:
            new_x = random.randint(0, self.width() - self.label.width())
            new_y = random.randint(0, self.height() - self.label.height())
            self.label.move(new_x, new_y)
        return super().eventFilter(source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTrackerApp()
    window.show()
    sys.exit(app.exec())
