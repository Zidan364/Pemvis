from PyQt6 import QtWidgets
from tugas4 import Ui_Form  # Impor UI
import sys

class MainApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Hubungkan tombol dengan fungsi
        self.pushButton.clicked.connect(self.add_to_cart)
        self.pushButton_2.clicked.connect(self.clear_cart)

        # Harga produk
        self.product_prices = {
            "Bimoli (Rp. 20,000)": 20000,
            "Beras 5 kg (Rp. 75,000)": 75000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Saos Saset (Rp. 2,500)": 2500
        }

        # Diskon dalam bentuk persentase
        self.discount_values = {
            "5%": 0.05,
            "10%": 0.10,
            "15%": 0.15
        }

        # Inisialisasi total harga
        self.total_price = 0

    def add_to_cart(self):
        """Menambahkan item ke keranjang dengan perhitungan diskon yang benar."""
        product = self.comboBox.currentText()
        quantity_text = self.lineEdit.text()
        discount_text = self.comboBox_2.currentText()

        # Validasi input
        if not quantity_text.isdigit():
            QtWidgets.QMessageBox.warning(self, "Input Error", "Quantity harus angka!")
            return

        quantity = int(quantity_text)
        if quantity <= 0:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Quantity harus lebih dari 0!")
            return

        # Ambil harga produk
        price = self.product_prices.get(product, 0)
        subtotal = price * quantity

        # Ambil nilai diskon
        discount = self.discount_values.get(discount_text, 0)
        discount_amount = subtotal * discount
        final_price = subtotal - discount_amount

        # Tambahkan ke list widget dengan format yang benar
        self.listWidget.addItem(f"{product} - {quantity} x Rp. {price:,.0f} (disc {discount_text})")

        # Update total harga
        self.total_price += final_price
        self.label_4.setText(f"Total : Rp. {self.total_price:,.0f}")

    def clear_cart(self):
        """Menghapus semua item dalam keranjang dan mengatur ulang total harga."""
        self.listWidget.clear()
        self.total_price = 0
        self.label_4.setText("Total : Rp. 0")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
