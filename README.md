# DataShield: Enkripsi Berbasis Kriptografi Kuantum

## 📌 Deskripsi
**DataShield** merupakan aplikasi eksperimental yang mengintegrasikan konsep kriptografi kuantum untuk melindungi data digital dengan pendekatan autentikasi kuantum dan pertukaran kunci berbasis simulasi. Aplikasi ini dirancang untuk meningkatkan keamanan data hingga ke tingkat teoritis yang paling tinggi.

---

## 🚀 Fitur Utama
1. **Simulasi Enkripsi Kuantum**
2. **Simulasi Protokol QKD (BB84)**
3. **Eksperimen GUI Kuantum menggunakan PyQt**

---

## 🧪 Teknologi yang Digunakan
- Python 3
- [Qiskit](https://qiskit.org/) – Untuk simulasi qubit dan QKD
- PyQt5 – GUI Desktop
- AES (Cryptography) – Enkripsi data menggunakan kunci dari QKD

---

## 🗂️ Struktur Folder
```
DataShield/
│
├── app/                  # Modul utama simulasi & enkripsi
├── ui/                   # GUI PyQt5
├── keys/                 # Penyimpanan kunci hasil QKD
├── simulation_data/      # Log kanal & penyadapan
├── tests/                # Unit test
├── main.py               # Entry point aplikasi
└── README.md             # Dokumentasi ini
```

---

## 🔧 Cara Menjalankan
1. Pastikan Python 3 sudah terinstal
2. Install dependensi:
```bash
pip install qiskit pyqt5 cryptography
```
3. Jalankan aplikasi:
```bash
python main.py
```

---

## 🧠 Konsep QKD yang Digunakan
Aplikasi ini menyimulasikan protokol **BB84**, yaitu:
- Alice mengirim qubit acak (0/1) dengan basis acak (Z/X)
- Bob mengukur dengan basis acak
- Basis disinkronisasi → didapat shared key
- Kunci ini dipakai untuk enkripsi AES

---

## 📂 File Penting
- `main.py` → Menjalankan GUI
- `qkd_simulator.py` → Simulasi pengiriman qubit
- `encryption_module.py` → Enkripsi & dekripsi data
- `channel_logger.py` → Simulasi kanal dan penyadapan

---

## 👨‍💻 Developer
> Raihan Nafis Zuraiq (6622600083)
> Sopi Marselia Dafina Putri (6622600079)
> Muti Meila Sari (6622600082)

---

## ⚠️ Catatan
Aplikasi ini adalah **simulasi**, bukan sistem kriptografi produksi. Semua proses terjadi secara lokal & virtual.
