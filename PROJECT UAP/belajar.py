import csv #membaca file csv, membaca setiap baris dalam file sebagai list
import tkinter as tk #untuk membuat Graphical User Interface (GUI) 
from tkinter import ttk, messagebox, filedialog

class Catatan: #untuk menggambarkan catatan pribadi
    def __init__(self, id_catatan, kategori, isi, tanggal): #atribut
        self.id_catatan = id_catatan #id unik untuk setiap catatan
        self.kategori = kategori #kategori catatan (keseharian, keuangan, kesehatan, pendidikan..)
        self.isi = isi #isi dari catatan
        self.tanggal = tanggal #tanggal catatan dilaksanakan

class ManajemenCatatan: #Mengelola semua operasi yang bisa dilakukan pada catatan.
    def __init__(self):
        self.catatan = [] #Daftar yang menyimpan semua objek Catatan.
        self.stack_dihapus = [] #untuk menyimpan catatan yang dihapus, memungkinkan pemulihan.

    def muat_catatan(self, filename): #Memuat/mengimpor catatan dari file CSV
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile: #membuka file csv
                reader = csv.reader(csvfile) #membaca file csv
                next(reader)  
                self.catatan = [Catatan(row[0], row[1], row[2], row[3]) for row in reader] #Buat objek Catatan untuk setiap baris dan tambahkan ke self.catatan.
        except FileNotFoundError: #Jika file tidak ditemukan, self.catatan akan diinisialisasi sebagai daftar kosong
            self.catatan = []

    def simpan_catatan(self, filename): #Menyimpan catatan ke file CSV.
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id_catatan', 'kategori', 'isi_catatan', 'tanggal'])
            for catatan in self.catatan:
                writer.writerow([catatan.id_catatan, catatan.kategori, catatan.isi, catatan.tanggal])

    def tambah_catatan(self, catatan):
        self.catatan.append(catatan) #Menambahkan catatan baru ke self.catatan

    def perbarui_catatan(self, id_catatan, kategori, isi, tanggal): #Memperbarui catatan yang sudah ada
        for catatan in self.catatan:
            if catatan.id_catatan == id_catatan: #cari catatan berdasarkan idi
                catatan.kategori = kategori #jika ditemukan, perbarui atributnya
                catatan.isi = isi
                catatan.tanggal = tanggal
                return True #Kembalikan True jika berhasil
        return False #Kembalikan False jika tidak ditemukan

    def hapus_catatan(self, id_catatan): #Menghapus catatan berdasarkan ID Catatan
        for catatan in self.catatan:
            if catatan.id_catatan == id_catatan: #cari berdasarkan id
                self.stack_dihapus.append(catatan)  # Tambahkan ke stack_dihapus
                self.catatan.remove(catatan) #hapus dari self.catatan
                return True #jika berhasil
        return False #jika id tidak ditemukan

    def cari_catatan(self, kunci, nilai): #Mencari catatan berdasarkan kategori atau tanggal.
        hasil = []
        if kunci == "kategori": #Jika kunci adalah kategori, cari yang mengandung nilai kategori.
            hasil = [catatan for catatan in self.catatan if nilai.lower() in catatan.kategori.lower()]
        elif kunci == "tanggal": #Jika kunci adalah tanggal, cari yang mengandung nilai tanggal.
            nilai_format = nilai.replace("-", "")
            hasil = [catatan for catatan in self.catatan if nilai_format in catatan.tanggal.replace("-", "")]
        return hasil

    def urutkan_catatan(self, kunci): #Mengurutkan catatan berdasarkan kategori atau tanggal.
        if kunci == "kategori": #Jika kunci adalah kategori, urutkan berdasarkan kategori
            self.catatan.sort(key=lambda catatan: catatan.kategori.lower())
        elif kunci == "tanggal": #Jika kunci adalah tanggal, urutkan berdasarkan tanggal dari yang terbaru
            self.catatan.sort(key=lambda catatan: catatan.tanggal.replace("-", ""), reverse=True)

    def pulihkan_catatan(self): #Memulihkan catatan yang dihapus.
        if self.stack_dihapus:
            catatan_dipulihkan = self.stack_dihapus.pop() #ambil catatan terakhir yang di hapus
            self.catatan.append(catatan_dipulihkan) #tambahkan kembali ke self.catatan
            return True
        return False #Memulihkan catatan yang dihapus.

#implementasi GUI
class Aplikasi(tk.Tk): #Membuat antarmuka pengguna menggunakan Tkinter.
    def __init__(self, manajemen_catatan):
        super().__init__()
        self.manajemen_catatan = manajemen_catatan
        self.title("Sistem Manajemen Catatan Pribadi")
        self.geometry("1200x700")

        self.style = ttk.Style(self)
        self.style.configure('TButton', padding=6, relief='flat', background='#ccc')
        self.style.configure('TFrame', padding=10)
        self.style.configure('Treeview', rowheight=25)
        self.style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.buat_widget()

    def buat_widget(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Kategori", "Isi", "Tanggal"), show='headings')
        self.tree.column("ID", width=100, anchor=tk.CENTER)
        self.tree.column("Kategori", width=100, anchor=tk.CENTER)
        self.tree.column("Isi", stretch=True)
        self.tree.column("Tanggal", width=100, anchor=tk.CENTER)
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Kategori", text="Kategori", anchor=tk.CENTER)
        self.tree.heading("Isi", text="Isi")
        self.tree.heading("Tanggal", text="Tanggal", anchor=tk.CENTER)
        self.tree.pack(expand=True, fill='both', pady=10, padx=10)

        self.frame = ttk.Frame(self) #menyimpan frame yang baru dibuat.
        self.frame.pack(fill='x') #memungkinkan widget diatur dalam orientasi (vertikal atau horizontal) Dengan fill='x', frame akan diperluas secara horizontal
        
        self.tombol_muat = ttk.Button(self.frame, text="Muat", command=self.muat_catatan)
        self.tombol_muat.pack(side='left', padx=5)

        self.tombol_simpan = ttk.Button(self.frame, text="Simpan", command=self.simpan_catatan)
        self.tombol_simpan.pack(side='left', padx=5)

        self.tombol_tambah = ttk.Button(self.frame, text="Tambah", command=self.tambah_catatan)
        self.tombol_tambah.pack(side='left', padx=5)

        self.tombol_perbarui = ttk.Button(self.frame, text="Perbarui", command=self.input_perbarui_catatan)
        self.tombol_perbarui.pack(side='left', padx=5)

        self.tombol_hapus = ttk.Button(self.frame, text="Hapus", command=self.hapus_catatan)
        self.tombol_hapus.pack(side='left', padx=5)

        self.tombol_cari = ttk.Button(self.frame, text="Cari", command=self.cari_catatan)
        self.tombol_cari.pack(side='left', padx=5)

        self.tombol_urutkan = ttk.Button(self.frame, text="Urutkan", command=self.urutkan_catatan)
        self.tombol_urutkan.pack(side='left', padx=5)

        self.tombol_pulihkan = ttk.Button(self.frame, text="Pulihkan", command=self.pulihkan_catatan)
        self.tombol_pulihkan.pack(side='left', padx=5)

    def muat_catatan(self): #Memuat catatan dari file CSV dan menampilkannya di Treeview
        filename = filedialog.askopenfilename(filetypes=[("File CSV", "*.csv")]) #Buka dialog untuk memilih file CSV
        if filename:
            self.manajemen_catatan.muat_catatan(filename) #Jika file dipilih, muat catatan menggunakan manajemen_catatan.
            self.perbarui_tree() #tampilkan catatan di Treeview.
            messagebox.showinfo("Sukses", "Catatan berhasil dimuat!")

    def simpan_catatan(self): #Menyimpan catatan ke file CSV.
        filename = filedialog.asksaveasfilename(filetypes=[("File CSV", "*.csv")]) #Buka dialog untuk menyimpan file CSV.
        if filename:
            self.manajemen_catatan.simpan_catatan(filename) #Jika file dipilih, simpan catatan menggunakan manajemen_catatan.
            messagebox.showinfo("Sukses", "Catatan berhasil disimpan!")

    def tambah_catatan(self): #Membuka jendela input untuk menambah catatan baru
        self.edit_catatan()

    def input_perbarui_catatan(self): #Membuka jendela input untuk memperbarui catatan yang sudah ada.
        self.jendela_perbarui = tk.Toplevel(self)
        self.jendela_perbarui.title("Perbarui Catatan")

        tk.Label(self.jendela_perbarui, text="Masukkan ID Catatan yang ingin diperbarui:").grid(row=0, column=0, padx=5, pady=5)
        self.id_perbarui = tk.Entry(self.jendela_perbarui)
        self.id_perbarui.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self.jendela_perbarui, text="Cari", command=self.konfirmasi_perbarui_catatan).grid(row=1, column=0, columnspan=2, pady=5)

    def konfirmasi_perbarui_catatan(self):
        id_catatan = self.id_perbarui.get()
        catatan = next((n for n in self.manajemen_catatan.catatan if n.id_catatan == id_catatan), None)
        if catatan:
            self.edit_catatan(catatan, id_catatan)
            self.jendela_perbarui.destroy()
        else:
            messagebox.showerror("Error", "ID Catatan tidak ditemukan!")
            self.jendela_perbarui.destroy()

    def hapus_catatan(self): #Menghapus catatan berdasarkan ID.
        self.input_hapus_catatan()

    def input_hapus_catatan(self):
        self.jendela_hapus = tk.Toplevel(self)
        self.jendela_hapus.title("Hapus Catatan")

        tk.Label(self.jendela_hapus, text="Masukkan ID Catatan yang ingin dihapus:").grid(row=0, column=0, padx=5, pady=5)
        self.id_hapus = tk.Entry(self.jendela_hapus)
        self.id_hapus.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self.jendela_hapus, text="Hapus", command=self.konfirmasi_hapus_catatan).grid(row=1, column=0, columnspan=2, pady=5)

    def konfirmasi_hapus_catatan(self):
        id_catatan = self.id_hapus.get()
        if self.manajemen_catatan.hapus_catatan(id_catatan): #panggil fungsi hapus_catatan dari manajemen_catatan
            self.perbarui_tree()
            messagebox.showinfo("Sukses", "Catatan berhasil dihapus!")
        else:
            messagebox.showerror("Error", "ID Catatan tidak ditemukan!")
        self.jendela_hapus.destroy()

    def cari_catatan(self):
        self.jendela_cari = tk.Toplevel(self)
        self.jendela_cari.title("Cari Catatan")

        tk.Label(self.jendela_cari, text="Cari Berdasarkan:").grid(row=0, column=0, padx=5, pady=5)
        self.kunci_cari = ttk.Combobox(self.jendela_cari, values=["kategori", "tanggal"])
        self.kunci_cari.grid(row=0, column=1, padx=5, pady=5)
        self.kunci_cari.current(0)

        tk.Label(self.jendela_cari, text="Nilai:").grid(row=1, column=0, padx=5, pady=5)
        self.nilai_cari = tk.Entry(self.jendela_cari)
        self.nilai_cari.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.jendela_cari, text="Cari", command=self.konfirmasi_cari_catatan).grid(row=2, column=0, columnspan=2, pady=5)

    def konfirmasi_cari_catatan(self):
        kunci = self.kunci_cari.get()
        nilai = self.nilai_cari.get()
        hasil = self.manajemen_catatan.cari_catatan(kunci, nilai) # panggil fungsi cari_catatan dari manajemen_catatan
        self.perbarui_tree(hasil) #Tampilkan hasil pencarian di Treeview.
        self.jendela_cari.destroy()

    def urutkan_catatan(self): #Mengurutkan catatan berdasarkan kategori atau tanggal.
        self.jendela_urutkan = tk.Toplevel(self)
        self.jendela_urutkan.title("Urutkan Catatan")

        tk.Label(self.jendela_urutkan, text="Urutkan Berdasarkan:").grid(row=0, column=0, padx=5, pady=5)
        self.kunci_urut = ttk.Combobox(self.jendela_urutkan, values=["kategori", "tanggal"])
        self.kunci_urut.grid(row=0, column=1, padx=5, pady=5)
        self.kunci_urut.current(0)

        ttk.Button(self.jendela_urutkan, text="Urutkan", command=self.konfirmasi_urutkan_catatan).grid(row=1, column=0, columnspan=2, pady=5)

    def konfirmasi_urutkan_catatan(self):
        kunci = self.kunci_urut.get()
        self.manajemen_catatan.urutkan_catatan(kunci) #panggil fungsi urutkan_catatan dari manajemen_catatan.
        self.perbarui_tree() #Tampilkan catatan yang sudah diurutkan di Treeview.
        self.jendela_urutkan.destroy()

    def pulihkan_catatan(self): #Memulihkan catatan yang dihapus.
        if self.manajemen_catatan.pulihkan_catatan(): #Panggil fungsi pulihkan_catatan dari manajemen_catatan.
            self.perbarui_tree()
            messagebox.showinfo("Sukses", "Catatan berhasil dipulihkan!")
        else:
            messagebox.showinfo("Info", "Tidak ada catatan yang bisa dipulihkan.")

    def edit_catatan(self, catatan=None, id_catatan=None): #untuk menambahkan atau mengedit catatan.
        self.jendela_edit = tk.Toplevel(self)
        self.jendela_edit.title("Tambah/Edit Catatan")

        tk.Label(self.jendela_edit, text="ID Catatan:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = tk.Entry(self.jendela_edit)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)
        if id_catatan:
            self.entry_id.insert(0, id_catatan)
            self.entry_id.config(state='disabled')
       
        tk.Label(self.jendela_edit, text="Kategori:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_kategori = tk.Entry(self.jendela_edit)
        self.entry_kategori = ttk.Combobox(self.jendela_edit, values=["keseharian", "keuangan", "kesehatan", "pendidikan", "hobi", "lainnya"])
        self.entry_kategori.grid(row=1, column=1, padx=5, pady=5)
        if catatan:
            self.entry_kategori.insert(0, catatan.kategori)
    
        tk.Label(self.jendela_edit, text="Isi Catatan:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_isi = tk.Text(self.jendela_edit, height=10, width=40)
        self.entry_isi.grid(row=2, column=1, padx=5, pady=5)
        if catatan:
            self.entry_isi.insert('1.0', catatan.isi)

        tk.Label(self.jendela_edit, text="Tanggal:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_tanggal = tk.Entry(self.jendela_edit)
        self.entry_tanggal.grid(row=3, column=1, padx=5, pady=5)
        if catatan:
            self.entry_tanggal.insert(0, catatan.tanggal)

        ttk.Button(self.jendela_edit, text="Simpan", command=lambda: self.konfirmasi_edit_catatan(catatan is not None)).grid(row=4, column=0, columnspan=2, pady=5)

    def konfirmasi_edit_catatan(self, memperbarui):
        id_catatan = self.entry_id.get()
        kategori = self.entry_kategori.get()
        isi = self.entry_isi.get("1.0", tk.END).strip()
        tanggal = self.entry_tanggal.get()

        if memperbarui:
            self.manajemen_catatan.perbarui_catatan(id_catatan, kategori, isi, tanggal)
            messagebox.showinfo("Sukses", "Catatan berhasil diperbarui!")
        else:
            catatan = Catatan(id_catatan, kategori, isi, tanggal)
            self.manajemen_catatan.tambah_catatan(catatan)
            messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan!")

        self.perbarui_tree() #memperbarui treeview
        self.jendela_edit.destroy()

    def perbarui_tree(self, data=None): #memperbarui tampilan data di treeview dengan data terbaru dari manajemen catatan.
        for i in self.tree.get_children():
            self.tree.delete(i) #Menghapus Semua Data di treeview
        if not data: #mengecek apakah argumen data yang diberikan adalah None atau kosong.
            data = self.manajemen_catatan.catatan #mengatur data menjadi daftar catatan dari objek manajemen_catatan
        for catatan in data: #Memasukkan data ke dalam treeview
            self.tree.insert("", "end", values=(catatan.id_catatan, catatan.kategori, catatan.isi, catatan.tanggal))

if __name__ == "__main__": #Bagian ini menjalankan aplikasi:
    manajemen_catatan = ManajemenCatatan() # membuat objek ManajemenCatatan
    app = Aplikasi(manajemen_catatan) #membuat objek aplikasi Aplikasi dengan manajemen_catatan sebagai argumen.
    app.mainloop() #menjalankan aplikasi Tkinter, memulai loop utama
