class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul   = judul
        self.penulis = penulis
        self.genre   = genre
        self.status  = status
        
    def __str__(self):
        return f"{self.judul} - karya : {self.penulis} - bergenre : {self.genre}- status : {self.status}"
        
class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []
        
    def check_ketersediaan(self):
        if not self.buku.tersedia:
            print(f"Buku {self.buku.judul}' tidak tersedia untuk dipinjam.")
        
    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("Koleksi buku masih kosong.")
            
    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
        print(f"Buku dengan judul '{judul} tidak ditemukan.")
             
    def pinjam_buku(self, judul, anggota):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                if buku.status == " Tersedia ":
                    anggota.buku_pinjaman.append(buku)
                    print(f"Buku '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
                    return
                elif buku.status == " Dipinjam ":
                    anggota.buku_pinjaman.append(buku)
                    print(f"Buku '{buku.judul}' sudah di pinjam oleh {anggota.nama}.")
                    return
                else:
                    print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")
                    return
        print(f"Buku dengan judul '{judul}' tidak ditemukan.")
    
class Anggota:
    def __init__(self, nama, ID, alamat=None, nomor_telepon=None):
        self.nama          = nama
        self.ID            = ID
        self.alamat        = alamat
        self.nomor_telepon = nomor_telepon
        self.buku_pinjaman = []
        
    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- Buku Pinjaman {self.nama} --")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")
            
class Catatan_peminjaman:
    def __init__(self, id_buku, id_anggota, tanggal_pinjam, tanggal_kembali):
        self.id_buku         = id_buku
        self.id_anggota      = id_anggota
        self.tanggal_pinjam  = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali          
            
def main():
    # Buat beberapa buku
    buku1 = Buku("Cantik Itu Luka", "Eka Kurniawan", "Fiksi", "Tersedia")
    buku2 = Buku("Laut Bercerita","Laila S.Chudori", "Fiksi", "Tersedia") 
    buku3 = Buku("Bumi Manusia", "Pramoedya Ananta Toer", "Drama history", "Tersedia")
    buku4 = Buku("Saman","Ayu Utami","Fiksi","Tersedia")
    buku5 = Buku("Ronggeng Dukuh Paruk","Ahmad Tohari","Fiksi","Tersedia")
    buku6 = Buku("Entrok","Okky Madasari","Fiksi","Dipinjam")
    buku7 = Buku("Sumur","Eka Kurniawan","Fiksi","Dipinjam")
    buku8 = Buku("Laskar Pelangi","Andrea Hirata","Fiksi","Dipinjam")
    buku9 = Buku("Tenggelamnya Kapal Van Der Wijick","Buya Hamka","Fiksi","Dipinjam")
    buku10 = Buku("Perjalan Menuju Pulang","Lala Bohang","Biografi","Dipinjam")

    # Buat perpustakaan
    perpustakaan = Perpustakaan() 
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3,buku4,buku5,buku6,buku7,buku8,buku9,buku10])
    
    # Buat anggota
    anggota1 = Anggota("kaa", 12345) 
    anggota2 = Anggota("ibad", 56789)

    # Jalankan program
    print("================================================")
    print("SELAMAT DATANG DI PROGRAM SEDERHANA PERPUSTAKAAN")
    print("by : Rifky Anshory")
    print("================================================")
    print()
    print("#-- Menu Perpustakaan --") 
    print("1. Tampilkan Daftar Buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    angka = int(input("Pilih menu : "))
    
    if angka == 1:
        perpustakaan.tampilkan_buku()
    elif angka == 2:
        judul = input("Masukkan judul buku : ")
        perpustakaan.cari_buku(judul)
    elif angka == 3:
        perpustakaan.tampilkan_buku()
        judul = input("Judul buku yang akan dipinjam : ")
        anggota = input("Masukkan nama anggota         : ")
        perpustakaan.pinjam_buku(judul, anggota)
    elif angka == 4:
        print("=======================================")
        print("Daftar buku yang sudah dipinjam")
        print("1. ",buku6)
        print("2. ",buku7)
        print("3. ",buku8)
        print("4. ",buku9)
        print("5. ",buku10)
        print("=======================================")
        print("KET : ")
        print("Jika anda ingin mengembalikan buku yang sudah anda pinjam,")
        print("mohon untuk memilih judul buku yg akan anda kembalikan,")
        angka = int(input("berdasarkan angka : "))
        if angka == 1:
            print("--------------------------------------------------------")
            print("Kami ucapkan Terima Kasih karna anda sudah mengembalikan")
            print("buku kami yg berjudul : Entrok karya dari Okky madasari")
            print("--------------------------------------------------------")
        elif angka == 2:
            print("--------------------------------------------------------")
            print("Kami ucapkan Terima Kasih karna anda sudah mengembalikan")
            print("buku kami yg berjudul : Sumur karya dari Eka kurniawan")
            print("--------------------------------------------------------")
        elif angka == 3:
            print("----------------------------------------------------------")
            print("Kami ucapkan Terima Kasih karna anda sudah mengembalikan")
            print("buku kami yg berjudul : Laskar pelangi karya Andrea Hirata")
            print("----------------------------------------------------------")
        elif angka == 4:
            print("------------------------------------------------------------------")
            print("Kami ucapkan Terima Kasih karna anda sudah mengembalikan buku kami")
            print("yg berjudul : Tenggelamnya kapal van der wijick karya Buya Hamka")
            print("-------------------------------------------------------------------")
        elif angka == 5:
            print("------------------------------------------------------------------")
            print("Kami ucapkan Terima Kasih karna anda sudah mengembalikan buku kami")
            print("yg berjudul : Perjalanan menuju pulang karya Lala Bohang")
            print("------------------------------------------------------------------")
        else:
            print("Maaf judul buku yg anda masukkan tidak terdaftar di dalam perpustakaan kami")
    else:
        print("Anda salah memilih.")
if __name__ == "__main__":
    main()
