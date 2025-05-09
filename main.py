import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStyleFactory
from PyQt5.QtGui import QIcon
from ui.main_dashboard import MainDashboard
from PyQt5.QtWidgets import QFileDialog, QMessageBox

def save_log(self):
    ciphertext = self.dashboard.output_box.toPlainText()

    if not ciphertext:
        QMessageBox.warning(self, "Peringatan", "Tidak ada data enkripsi untuk disimpan.")
        return

    options = QFileDialog.Options()
    filepath, _ = QFileDialog.getSaveFileName(self, "Simpan Log Enkripsi", "", "Text Files (*.txt);;All Files (*)", options=options)
    
    if filepath:
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write("===== Hasil Enkripsi DataShield =====\n")
                file.write(ciphertext)
            QMessageBox.information(self, "Berhasil", "Log enkripsi berhasil disimpan.")
        except Exception as e:
            QMessageBox.critical(self, "Gagal", f"Gagal menyimpan file:\n{e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DataShield - Quantum Encryption Simulator")
        self.setMinimumSize(900, 600)

        # Tambahkan ikon aplikasi (pastikan file 'icon.png' ada di folder yang sama dengan main.py)
        self.setWindowIcon(QIcon("icon.png"))

        # Muat tampilan utama
        self.dashboard = MainDashboard()
        self.setCentralWidget(self.dashboard)

        # Tambahkan menu bar
        self.init_menu()

    def init_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        help_menu = menubar.addMenu("Bantuan")

        exit_action = QAction("Keluar", self)
        exit_action.triggered.connect(self.close)

        about_action = QAction("Tentang", self)
        about_action.triggered.connect(self.show_about)

        file_menu.addAction(exit_action)
        help_menu.addAction(about_action)

    def show_about(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Tentang Aplikasi", "DataShield - Simulator Enkripsi Kuantum\nDibuat oleh Nafis, Sofi, dan Muti (2025)")

def main():
    app = QApplication(sys.argv)

    # Terapkan tema gelap
    app.setStyle("Fusion")
    dark_palette = app.palette()
    dark_palette.setColor(app.palette().Window,       app.palette().color(app.palette().Window).darker(150))
    dark_palette.setColor(app.palette().Base,         app.palette().color(app.palette().Base).darker(180))
    dark_palette.setColor(app.palette().AlternateBase,app.palette().color(app.palette().AlternateBase).darker(150))
    dark_palette.setColor(app.palette().Button,       app.palette().color(app.palette().Button).darker(150))
    app.setPalette(dark_palette)

    # Tampilkan window utama
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
