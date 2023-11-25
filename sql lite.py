import tkinter as tk
import sqlite3 

def hasil_prediksi():
    # Mendapatkan nilai dari input
    nama = entry_nama.get()

    # Mendapatkan nilai dari 10 mata pelajaran (3 yang sudah ada + 10 tambahan)
    try:
        nilai_biologi = float(entry_biologi.get())
        nilai_fisika = float(entry_fisika.get())
        nilai_inggris = float(entry_inggris.get())
        nilai_matematika = float(entry_matematika.get())
        nilai_kimia = float(entry_kimia.get())
        nilai_sejarah = float(entry_sejarah.get())
        nilai_geografi = float(entry_geografi.get())
        nilai_seni = float(entry_seni.get())
        nilai_olahraga = float(entry_olahraga.get())
        nilai_ekonomi = float(entry_ekonomi.get())
    except ValueError:
        # Handle the case where the input is not a valid float
        # You can show an error message or take appropriate action
        print("Invalid input. Please enter valid numeric values.")
        return
    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    # Membandingkan nilai dari 13 mata pelajaran
    nilai_tinggi = max(nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia,
                       nilai_sejarah, nilai_geografi, nilai_seni, nilai_olahraga,
                       nilai_ekonomi)

    if nilai_tinggi == nilai_biologi:
        hasil_fakultas = "Kedokteran"
    elif nilai_tinggi == nilai_fisika:
        hasil_fakultas = "Teknik"
    elif nilai_tinggi == nilai_inggris:
        hasil_fakultas = "Bahasa"
    elif nilai_tinggi == nilai_matematika:
        hasil_fakultas = "FMIPA"
    elif nilai_tinggi == nilai_kimia:
        hasil_fakultas = "FMIPA"
    elif nilai_tinggi == nilai_sejarah:
        hasil_fakultas = "Ilmu Sosial"
    elif nilai_tinggi == nilai_geografi:
        hasil_fakultas = "FMIPA"
    elif nilai_tinggi == nilai_seni:
        hasil_fakultas = "Ilmu Budaya"
    elif nilai_tinggi == nilai_olahraga:
        hasil_fakultas = "Keolahragaan"
    elif nilai_tinggi == nilai_ekonomi:
        hasil_fakultas = "FEB"
        
    # Tambahkan kondisi untuk prodi berdasarkan nilai tertinggi dari mata pelajaran lainnya

    else:
        hasil_fakultas = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil.config(text=f"Prodi Pilihan: {hasil_fakultas}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('prediksi_fakultas_.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS prediksi_fakultas (
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
                        ekonomi REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute('''INSERT INTO prediksi_fakultas (nama_siswa, biologi, fisika, inggris, matematika,
                    kimia, sejarah, geografi, seni, olahraga, ekonomi, prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nama, nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia,
                    nilai_sejarah, nilai_geografi, nilai_seni, nilai_olahraga,
                    nilai_ekonomi, hasil_fakultas))
    conn.commit()
    conn.close()

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")  # Mengatur ukuran jendela

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)

# Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa: ")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Membuat 10 label dan entry baru untuk 10 mata pelajaran tambahan
label_biologi = tk.Label(root, text="Nilai Biologi: ")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika: ")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris: ")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

label_matematika = tk.Label(root, text="Nilai Matematika: ")
label_matematika.pack()
entry_matematika = tk.Entry(root)
entry_matematika.pack()

label_kimia = tk.Label(root, text="Nilai Kimia: ")
label_kimia.pack()
entry_kimia = tk.Entry(root)
entry_kimia.pack()

label_sejarah = tk.Label(root, text="Nilai Sejarah: ")
label_sejarah.pack()
entry_sejarah = tk.Entry(root)
entry_sejarah.pack()

label_geografi = tk.Label(root, text="Nilai Geografi: ")
label_geografi.pack()
entry_geografi = tk.Entry(root)
entry_geografi.pack()

label_seni = tk.Label(root, text="Nilai Seni: ")
label_seni.pack()
entry_seni = tk.Entry(root)
entry_seni.pack()

label_olahraga = tk.Label(root, text="Nilai Olahraga: ")
label_olahraga.pack()
entry_olahraga = tk.Entry(root)
entry_olahraga.pack()

label_ekonomi = tk.Label(root, text="Nilai Ekonomi: ")
label_ekonomi.pack()
entry_ekonomi = tk.Entry(root)
entry_ekonomi.pack()

# Button Submit Nilai
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi)
button_submit.pack(pady=10)

# Label luaran hasil prediksi
hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil.pack()

root.mainloop()