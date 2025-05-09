from PyQt5.QtWidgets import (
    QWidget, QLabel, QTextEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from app.qkd_simulator import simulate_qkd
from app.encryption_module import encrypt_message, decrypt_message
import base64
class MainDashboard(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("DataShield - Dashboard")
        self.setMinimumSize(600, 400)

        self.qkd_key = None
        self.encrypted_text = ""

        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()

        # Input pesan
        self.input_label = QLabel("Masukkan pesan untuk dienkripsi:")
        self.input_text = QTextEdit()

        # Tombol-tombol
        button_layout = QHBoxLayout()
        self.encrypt_btn = QPushButton("🔐 Enkripsi")
        self.decrypt_btn = QPushButton("🔓 Dekripsi")
        self.visualize_btn = QPushButton("👁️ Visualisasi QKD")

        self.encrypt_btn.clicked.connect(self.encrypt_message)
        self.decrypt_btn.clicked.connect(self.decrypt_message)
        self.visualize_btn.clicked.connect(self.visualize_qkd)

        button_layout.addWidget(self.encrypt_btn)
        button_layout.addWidget(self.decrypt_btn)
        button_layout.addWidget(self.visualize_btn)

        # Output hasil
        self.result_label = QLabel("Hasil:")
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        # Gabungkan semua ke layout
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def encrypt_message(self):
        plain_text = self.input_text.toPlainText()
        if not plain_text:
            QMessageBox.warning(self, "Peringatan", "Pesan tidak boleh kosong.")
            return

        self.qkd_key = simulate_qkd()
        if len(self.qkd_key) < 16:
            QMessageBox.warning(self, "Kunci QKD Gagal", "Kunci terlalu pendek.")
            return

        key_bytes = bytes(self.qkd_key[:16])
        self.encrypted_text = encrypt_message(plain_text, key_bytes)

        self.result_text.setPlainText(f"Pesan terenkripsi:\n{self.encrypted_text}")

    def decrypt_message(self):
        if not self.encrypted_text or not self.qkd_key:
            QMessageBox.warning(self, "Gagal", "Belum ada pesan terenkripsi atau kunci QKD.")
            return

        key_bytes = bytes(self.qkd_key[:16])
        try:
            decrypted = decrypt_message(self.encrypted_text, key_bytes)
            self.result_text.setPlainText(f"Pesan terdekripsi:\n{decrypted}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Dekripsi gagal: {str(e)}")

    def visualize_qkd(self):
        if not self.qkd_key:
            QMessageBox.information(self, "QKD Belum Ada", "Silakan lakukan enkripsi untuk menghasilkan kunci QKD.")
            return
    
        bit_string = ''.join(map(str, self.qkd_key[:16]))
        QMessageBox.information(self, "Visualisasi Kunci QKD", f"Kunci QKD (16-bit):\n{bit_string}")
