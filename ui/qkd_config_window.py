from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox, QCheckBox

class QKDConfigWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konfigurasi QKD")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.basis_label = QLabel("Pilih basis:")
        self.basis_choice = QComboBox()
        self.basis_choice.addItems(["Acak", "Z", "X"])

        self.visual_checkbox = QCheckBox("Aktifkan visualisasi qubit")

        layout.addWidget(self.basis_label)
        layout.addWidget(self.basis_choice)
        layout.addWidget(self.visual_checkbox)
        self.setLayout(layout)
