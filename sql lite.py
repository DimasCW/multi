import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai
def prediksi_fakultas(nilai):
    # Mendapatkan nama mata pelajaran dengan nilai tertinggi
    mata_pelajaran = max(nilai, key=lambda k: nilai[k])
    
    # Mapping mata pelajaran ke fakultas
    mapping_fakultas = {
        "Biologi": "Kedokteran",
        "Fisika": "Teknik",
        "Inggris": "Bahasa",
        "Matematika": "Matematika",
        "Kimia": "Kimia",
        "Sejarah": "Sejarah",
        "Geografi": "Geografi",
        "Seni": "Seni",
        "Olahraga": "Olahraga",
        "Ekonomi": "Ekonomi"
    }

    return mapping_fakultas.get(mata_pelajaran, "Tidak dapat memprediksi fakultas")

# Inisialisasi database SQLite
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Membuat tabel nilai_siswa jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_siswa TEXT,
        biologi REAL,
        fisika REAL,
        inggris REAL,
        matematika REAL,
        kimia REAL,
        sejarah REAL,
        geografi REAL,
        seni REAL,
        olahraga REAL,
        ekonomi REAL
    )
''')
conn.commit()

# Fungsi untuk menangani tombol submit
def submit_nilai():
    # Mendapatkan nilai dari input
    nama_siswa = entry_nama.get()
    nilai_biologi = float(entry_nilai["Biologi"].get())
    nilai_fisika = float(entry_nilai["Fisika"].get())
    nilai_inggris = float(entry_nilai["Inggris"].get())
    nilai_matematika = float(entry_nilai["Matematika"].get())
    nilai_kimia = float(entry_nilai["Kimia"].get())
    nilai_sejarah = float(entry_nilai["Sejarah"].get())
    nilai_geografi = float(entry_nilai["Geografi"].get())
    nilai_seni = float(entry_nilai["Seni"].get())
    nilai_olahraga = float(entry_nilai["Olahraga"].get())
    nilai_ekonomi = float(entry_nilai["Ekonomi"].get())

    # Menambahkan data siswa ke dalam database
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, matematika, kimia, sejarah, geografi, seni, olahraga, ekonomi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia, nilai_sejarah, nilai_geografi, nilai_seni, nilai_olahraga, nilai_ekonomi))
    conn.commit()

    # Menampilkan pesan bahwa data telah ditambahkan
    messagebox.showinfo("Sukses", f"Data nilai untuk {nama_siswa} berhasil ditambahkan!")

    # Mengosongkan input setelah data ditambahkan
    entry_nama.delete(0, tk.END)
    for key in entry_nilai:
        entry_nilai[key].delete(0, tk.END)

# Fungsi untuk melakukan prediksi fakultas berdasarkan nilai tertinggi
def prediksi_fakultas_iterasi():
    cursor.execute('SELECT * FROM nilai_siswa')
    data_nilai_siswa = cursor.fetchall()

    if not data_nilai_siswa:
        messagebox.showwarning("Peringatan", "Belum ada data nilai siswa yang dimasukkan!")
        return

    for data_siswa in data_nilai_siswa:
        nama_siswa = data_siswa[1]
        nilai_siswa = {
            "Biologi": data_siswa[2],
            "Fisika": data_siswa[3],
            "Inggris": data_siswa[4],
            "Matematika": data_siswa[5],
            "Kimia": data_siswa[6],
            "Sejarah": data_siswa[7],
            "Geografi": data_siswa[8],
            "Seni": data_siswa[9],
            "Olahraga": data_siswa[10],
            "Ekonomi": data_siswa[11]
        }
        prediksi = prediksi_fakultas(nilai_siswa)

        # Menampilkan hasil prediksi fakultas di bawah tombol submit
        label_hasil.config(text=f"Prediksi fakultas untuk {nama_siswa}: {prediksi}")

# Membuat GUI menggunakan tkinter
root = tk.Tk()
root.title("Prediksi Fakultas")

# Label dan Entry untuk input nama siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.grid(row=0, column=0, padx=10, pady=10)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

# Entry untuk setiap mata pelajaran
mata_pelajaran = ["Biologi", "Fisika", "Inggris", "Matematika", "Kimia", "Sejarah", "Geografi", "Seni", "Olahraga", "Ekonomi"]
entry_nilai = {}
row_counter = 1
for pelajaran in mata_pelajaran:
    label_pelajaran = tk.Label(root, text=f"Nilai {pelajaran}:")
    label_pelajaran.grid(row=row_counter, column=0, padx=10, pady=10)
    entry_nilai[pelajaran] = tk.Entry(root)
    entry_nilai[pelajaran].grid(row=row_counter, column=1, padx=10, pady=10)
    row_counter += 1

# Tombol Submit
button_submit = tk.Button(root, text="Submit", command=submit_nilai)
button_submit.grid(row=row_counter, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi fakultas
label_hasil = tk.Label(root, text="")
label_hasil.grid(row=row_counter + 1, column=0, columnspan=2, pady=10)

# Tombol untuk menampilkan prediksi fakultas
button_prediksi = tk.Button(root, text="Prediksi Fakultas", command=prediksi_fakultas_iterasi)
button_prediksi.grid(row=row_counter + 2, column=0, columnspan=2, pady=10)

# Menjalankan program
root.mainloop()
