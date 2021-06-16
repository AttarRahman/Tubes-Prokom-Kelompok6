# PROGRAM PENYEWAAN DAN PEMBELIAN KASET
import sys
import time
import datetime
# Nomor kartu peminjaman
import random
nomor_pinjam = random.randrange(1, 10 ** 6)
nomor_kartupeminjaman = '{:08}'.format(nomor_pinjam)

# Data List
nama_plgn = []
nik_plgn = []
tempat_lahir = []
tanggal_lahir = []
nomor_telefon = []
alamat = []
bio_kaset = {}
jaminan = []

def halamanutama():
    JudulProgram1 = "PROGRAM SEWA & BELI KASET"
    JudulProgram2 = "TOKO INDENTURE DISC"
    print(50 * "=")
    print(JudulProgram1.center(50))
    print(JudulProgram2.center(50))
    print(50 * "=")

def login():
    global nama_plgn
    global nik_plgn
    print('\n')
    jdl_login = "####   Login Member   ####"
    print(jdl_login.center(50))
    nama_plgn = input("Nama member = ")
    nik_plgn = input("NIK         = ")
    print(50 * "-")

def registrasi():
    global nama_plgn, nik_plgn, tempat_lahir, tanggal_lahir, nomor_telefon, alamat
    if (Que2.upper() == "Y"):
        jdl_reg = "####   Registrasi Member   ####"
        print("\n", jdl_reg.center(50))
        nama_plgn = input("Masukkan nama Anda = ")
        nik_plgn = input("Masukkan NIK Anda = ")
        tempat_lahir = input("Tempat lahir = ")
        tanggal_lahir = input("Tanggal lahir (contoh : 11 Januari 2002) = ")
        nomor_telefon = input("Masukkan nomor telefon Anda = ")
        alamat = input("Alamat Rumah = ")
        # memastikan data yang dimasukkan benar
        print(50 * "=")
        print("Pastikan data yang anda masukkan sudah benar.\n")
        print("Nama = ", nama_plgn)
        print("NIK = ", nik_plgn)
        print("Tempat/Tanggal lahir = ", tempat_lahir, ",", tanggal_lahir)
        print("Nomor telefon = ", nomor_telefon)
        print("Alamat = ", alamat)
        print(50 * "_")
        biodata = """\nNama = {}\nNIK = {}\nTempat/Tanggal lahir = {}\nNomor Telefon = {}
Alamat = {}\n""".format(nama_plgn, nik_plgn, tempat_lahir + "," + tanggal_lahir, nomor_telefon, alamat)
        database = open("databasemember.txt", "a")
        database.write(biodata)
        database.close()
    else:
        pass

def show_menu_nonmember():
    print("\n")
    judul_menu = "Pilih Menu"
    print(judul_menu.center(50, '-'))
    print("[1]  Peminjaman Kaset")
    print("[2]  Pengembalian Kaset")
    print("[3]  Pembelian Kaset")
    print("[4]  Keluar")
    print(50 * "-")
    pilih_menu = input("Pilih menu --> ")
    print("\n")

    if pilih_menu == '1':
        PeminjamanNonmember()
    elif pilih_menu == '2':
        PengembalianNonMember()
    elif pilih_menu == '3':
        Pembelian()
    elif pilih_menu == '4':
        halamanutama()
        sys.exit()
    else:
        print("Maaf nomor yang Anda masukkan tidak ada!!")

def show_menu_member():
    print("\n")
    judul_menu = "Pilih Menu"
    print(judul_menu.center(50, "-"))
    print("[1]  Peminjaman Kaset")
    print("[2]  Pengembalian Kaset")
    print("[3]  Pembelian Kaset")
    print("[4]  Keluar")
    print(50 * "-")
    pilih_menu = input("Pilih menu --> ")
    print("\n")

    if pilih_menu == '1':
        PeminjamanMember()
    elif pilih_menu == '2':
        PengembalianMember()
    elif pilih_menu == '3':
        Pembelian()
    elif pilih_menu == '4':
        halamanutama()
        sys.exit()
    else:
        print("Maaf nomor yang Anda masukkan tidak ada!!")

def Tabel_hargasewa():
    print('''
    ___________________________________________________
    |  No |   Genre Film   |  Kode Film  | Harga Beli |
    ---------------------------------------------------
    |  1. |  Thriller      |      A      |    8000    | 
    |  2. |  Comedy        |      B      |    6000    |
    |  3. |  Romance       |      C      |    6000    |
    |  4. |  Action        |      D      |    7000    |
    |  5. |  Drama         |      E      |    5000    |
    --------------------------------------------------- ''')

def Formulirsewa_member():
    global jaminan, bio_kaset
    print("\nSilahkan masukkan data dibawah ini untuk melengkapi langkah peminjaman kaset")
    bio_kaset['Nama kaset'] = input('\nMasukkan nama kaset Anda    = ')
    bio_kaset['Kode kaset'] = input('Masukkan kode kaset Anda    = ')
    bio_kaset['Genre kaset'] = input('Masukkan genre kaset Anda   = ')
            sys.exit()
    else:
        Formulir_sewa()

def StrukPeminjamanKasetMember():
    Kode_kaset = bio_kaset['Kode kaset']
    jumlahpesan = bio_kaset['Jumlah kaset']
    if Kode_kaset == "A":
        #Genre Kaset = 'Thriller'
        Genre_kaset = 'Thriller'
        harga = (8000 * jumlahpesan)/2
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif Kode_kaset == "B":
        #Genre kaset = 'Comedy'
        Genre_kaset = 'Comedy'
        harga = (6000 * jumlahpesan)/2
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif Kode_kaset == "C":
        #Genre kaset = 'Romance'
        Genre_kaset = 'Romance'
        harga = (6000 * jumlahpesan)/2
        diskon = int(harga * 0.1)
        totalharga = int((0.5)*harga - diskon)
    elif Kode_kaset == "D":
        #Genre kaset = 'Action'
        Genre_kaset = 'Action'
        harga = (7000 * jumlahpesan)/2
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif Kode_kaset == "E":
        #Genre kaset = 'Drama'
        Genre_kaset = 'Drama'
        harga = (5000 * jumlahpesan)/2
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    else:
        Genre_kaset = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
    print(""" 
    Untuk melakukan transaksi pembayaran silahkan pilih metode pembayaran Anda!
    ==============================
     A. Tunai
     B. Ovo
     C. Transfer 
     D. Dana
    ==============================
     """)
    menupembayaran = str(input("Pilih metode pembayaran Anda = "))
    if menupembayaran == "A":
        #print("Tunai")
        bayar = int(input("=== Masukkan uang Anda = "))
        print("\n")
        print("="*45)
        nama = "STRUK PEMBAYARAN"
        nama2 = "INDENTURE DISC"
        print(nama.center(45, "="))
        print(nama2.center(45))
        print("=" * 45)
        print("\nPeminjaman Kaset :")
        print(bio_kaset['Nama kaset'], "(%s)"%(Genre_kaset), "x", jumlahpesan,"    ", harga)
        print("-"*45)
        print("Total Harga                      ", harga)
        print("Total Bayar                      ", totalharga)
        print("Tunai                            ", bayar)
        print("Diskon 10%                       ", diskon)
        print("Tunai                            ", bayar)
        print("Kembalian                        ", bayar - totalharga)
        print("Kode Peminjaman                  ", nomor_kartupeminjaman)
        print("-"*45)
        print("\n==========================Terimakasih,Selamat Datang Kembali=========================")

    else:
        print("\n")
        print("=" * 45)
        nama = "STRUK PEMBAYARAN"
        nama2 = "INDENTURE DISC"
        print(nama.center(45, "="))
        print(nama2.center(45))
        print("=" * 45)
        print("\nPeminjaman Kaset :")
        print(bio_kaset['Nama kaset'], "(%s)" % (Genre_kaset), "x", jumlahpesan, "    ", harga)
        print("-" * 45)
        print("Total Harga                      ", harga)
        print("Diskon 10%                       ", diskon)
        print("Total Bayar                      ", totalharga)
        print("Menu Pembayaran    :", menupembayaran)
        print("Kode Peminjaman                  ", nomor_kartupeminjaman)
        print("-" * 45)
        print("Silahkan Melakukan Pembayaran Segera !! ")
        print(""" 
                _________________________________
                |Note:                          |
                | 1. Ovo =345546744534          |
                | 2. Tranfer = 23456646543236664|
                | 3. Dana = 4353466754          | 
                ---------------------------------   
                      """)
        print("\n==========================Terimakasih,Selamat Datang Kembali=========================")

def StrukPeminjamanPembelianNonMember():
    Kode_kaset = bio_kaset['Kode kaset']
    jumlahpesan = bio_kaset['Jumlah kaset']
    if Kode_kaset == "A":
        #Genre Kaset = 'Thriller'
        Genre_kaset = 'Thriller'
        harga = (8000 * jumlahpesan)/2
        diskon = 0
        totalharga = int(harga - diskon)
    elif Kode_kaset == "B":
        #Genre kaset = 'Comedy'
        Genre_kaset = 'Comedy'
        harga = (6000 * jumlahpesan)/2
        diskon = 0
        totalharga = int(harga - diskon)
    elif Kode_kaset == "C":
        #Genre kaset = 'Romance'
        Genre_kaset = 'Romance'
        harga = (6000 * jumlahpesan)/2
        diskon = 0
        totalharga = int(harga - diskon)
    elif Kode_kaset == "D":
        #Genre kaset = 'Action'
        Genre_kaset = 'Action'
        harga = (7000 * jumlahpesan)/2
        diskon = 0
        totalharga = int(harga - diskon)
    elif Kode_kaset == "E":
        #Genre kaset = 'Drama'
        Genre_kaset = 'Drama'
        harga = (5000 * jumlahpesan)/2
        diskon = 0
        totalharga = int(harga - diskon)
    else:
        Genre_kaset = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
    print(""" Untuk melakukan transaksi pembayaran silahkan pilih metode pembayaran Anda!
    ==============================
     A. Tunai
     B. Ovo
     C. Transfer 
     D. Dana
    ==============================
     """)
    menupembayaran = str(input("Pilih metode pembayaran Anda = "))
    if menupembayaran == "A":
        #print("Tunai")
        bayar = int(input("=== Masukkan uang Anda = "))
        print("\n")
        print("="*45)
        nama = "STRUK PEMBAYARAN"
        nama2 = "INDENTURE DISC"
        print(nama.center(45, "="))
        print(nama2.center(45))
        print("=" * 45)
        print("\nPeminjaman Kaset :")
        print(bio_kaset['Nama kaset'], "(%s)"%(Genre_kaset), "x", jumlahpesan,"    ", harga)
        print("-"*45)
        print("Total Harga                      ", harga)
        print("Total Bayar                      ", totalharga)
        print("Tunai                            ", bayar)
        print("Diskon 10%                       ", diskon)
        print("Tunai                            ", bayar)
        print("Kembalian                        ", bayar - totalharga)
        print("Kode Peminjaman                  ", nomor_kartupeminjaman)
        print("-"*45)
        print("\n==========================Terimakasih,Selamat Datang Kembali=========================")
    else:
        #metode non tunai
        print("\n")
        print("=" * 45)
        nama = "STRUK PEMBAYARAN"
        nama2 = "INDENTURE DISC"
        print(nama.center(45, "="))
        print(nama2.center(45))
        print("=" * 45)
        print("\nPeminjaman Kaset :")
        print(bio_kaset['Nama kaset'], "(%s)" % (Genre_kaset), "x", jumlahpesan, "    ", harga)
        print("-" * 45)
        print("Total Harga                      ", harga)
        print("Diskon 10%                       ", diskon)
        print("Total Bayar                      ", totalharga)
        print("Menu Pembayaran    :", menupembayaran)
        print("Kode Peminjaman                  ", nomor_kartupeminjaman)
        print("-" * 45)
        print("Silahkan Melakukan Pembayaran Segera !! ")
        print(""" 
                _________________________________
                |Note:                          |
                | 1. Ovo =345546744534          |
                | 2. Tranfer = 23456646543236664|
                | 3. Dana = 4353466754          | 
                ---------------------------------   
                      """)
        print("\n==========================Terimakasih,Selamat Datang Kembali=========================")

def IsikartuPeminjamandanPengembalian():
    print("  Nomor Nota           = ", nomor_kartupeminjaman)
    print("  NIK                  = ", nik_plgn)
    print("  Alamat               = ", bio_plgn['Alamat'])
    print("  Nama Kaset           = ", bio_kaset['Nama kaset'])
    print("  Kode Kaset           = ", bio_kaset['Kode kaset'])
    print("  Genre Kaset          = ", bio_kaset['Genre kaset'])
    print(tanggal_pinjam.strftime("  Tanggal Kembali     = %d/%m/%Y, %H:%M:%S"))
    print(tanggal_kembali.strftime("  Tanggal Kembali     = %d/%m/%Y, %H:%M:%S"))

def PengembalianMember():
    nomor_kartupeminjaman = input("Masukkan nomor kartu peminjaman Anda = ")
    print("Apakah benar %s nomor kartu peminjaman Anda? (y/t)" %(nomor_kartupeminjaman))
    cek2 = input(">>> ")
    if cek2 == "y":
        print("""
______________________________________________________________
|              KARTU PENGEMBALIAN INDENTURE DISC             |
|                 Jln.Gagak No.15, Surakarta                 |
--------------------------------------------------------------
                """)

        IsikartuPeminjamandanPengembalian()
        cekb = input("Apakah Anda ingin melanjutkan transaksi pembayaran? (y/t) = ")
        if cekb == "y":
            StrukPeminjamanKasetMember()
            cekc = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
            if cekc == "y":
                show_menu_member()
        else:
            sys.exit()
    else:
        PengembalianMember()

def PengembalianNonMember():
    nomor_kartupeminjaman = input("Masukkan nomor kartu peminjaman Anda = ")
    print("Apakah benar %s nomor kartu peminjaman Anda? (y/t)" % (nomor_kartupeminjaman))
    cek2 = input(">>> ")
    if cek2 == "y":
        print("""
______________________________________________________________
|              KARTU PENGEMBALIAN INDENTURE DISC             |
|                 Jln.Gagak No.15, Surakarta                 |
--------------------------------------------------------------

                """)
        IsikartuPeminjamandanPengembalian()
        cek3 = input("Apakah Anda ingin melanjutkan transaksi pembayaran? (y/t) = ")
        if cek3 == 'y':
            StrukPeminjamanPembelianNonMember()
            cek4 = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
            if cek4 == "y":
                show_menu_nonmember()
        else:
            sys.exit()
    else:
        PengembalianNonMember()

def PembelianMember():
    print("""
    ====================================================

                    TOKO INDENTURE DISC
                    Daftar Harga Kaset

    ====================================================
        A. Thriller : Rp 30.000
        B. Comedy   : Rp 25.000
        C. Romance  : Rp 50.000
        D. Action   : Rp 40.000
        E. Drama    : Rp 60.000
    ====================================================
        """)
    pesan = str(input("Masukkan Genre kaset yang ingin dibeli = "))
    jumlahpesan = int(input("Masukkan jumlah pesanan = "))
    if pesan == "A":
        Genre_kaset = "Thriller"
        harga = (30000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif pesan == "B":
        Genre_kaset = "Comedy"
        harga = (25000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif pesan == "C":
        Genre_kaset = "Romance"
        harga = (50000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif pesan == "D":
        Genre_kaset = "Action"
        harga = (40000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif pesan == "e":
        Genre_kaset = "Drama"
        harga = (60000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    else:
        Genre_kaset = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        print("Menu tidak tersedia")

    print("--------------------------")
    print("Toko Indenture Disc")
    print("--------------------------")
    print("Menu :", Genre_kaset)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
        
def pembelianNonMember():
    print("""
    ====================================================

                    TOKO INDENTURE DISC
                    Daftar Harga Kaset

    ====================================================
        A. Thriller : Rp 30.000
        B. Comedy   : Rp 25.000
        C. Romance  : Rp 50.000
        D. Action   : Rp 40.000
        E. Drama    : Rp 60.000
    ====================================================
        """)
    pesan = str(input("Masukkan Genre kaset yang ingin dibeli = "))
    jumlahpesan = int(input("Masukkan jumlah pesanan = "))
    if pesan == "A":
        Genre_kaset = "Thriller"
        harga = (30000 * jumlahpesan)
        diskon = (0)
        totalharga = int(harga)
    elif pesan == "B":
        Genre_kaset = "Comedy"
        harga = (25000 * jumlahpesan)
        diskon = (0)
        totalharga = int(harga)
    elif pesan == "C":
        Genre_kaset = "Romance"
        harga = (50000 * jumlahpesan)
        diskon = (0)
        totalharga = int(harga)
    elif pesan == "D":
        Genre_kaset = "Action"
        harga = (40000 * jumlahpesan)
        diskon = (0)
        totalharga = int(harga)
    elif pesan == "e":
        Genre_kaset = "Drama"
        harga = (60000 * jumlahpesan)
        diskon = (0)
        totalharga = int(harga)
    else:
        Genre_kaset = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        print("Menu tidak tersedia")

    print("--------------------------")
    print("Toko Indenture Disc")
    print("--------------------------")
    print("Menu :", Genre_kaset)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")

def show_menu_member():
    print("\n")
    judul_menu = "Pilih Menu"
    print(judul_menu.center(50, '-'))
    print("[1]  Peminjaman Kaset")
    print("[2]  Pengembalian Kaset")
    print("[3]  Pembelian Kaset")
    print("[4]  Keluar")
    pilih_menu = input("Pilih menu --> ")
    print("\n")

    if pilih_menu == '1':
        PeminjamanMember()
    elif pilih_menu == '2':
        PengembalianMember()
    elif pilih_menu == '3':
        PembelianMember()
    elif pilih_menu == '4':
        sys.exit()
    else:
        print("Maaf nomor yang Anda masukkan tidak ada!!")

def show_menu_nonmember():
    print("\n")
    judul_menu = "Pilih Menu"
    print(judul_menu.center(50, '-'))
    print("[1]  Peminjaman Kaset")
    print("[2]  Pengembalian Kaset")
    print("[3]  Pembelian Kaset")
    print("[4]  Keluar")
    pilih_menu = input("Pilih menu --> ")
    print("\n")

    if pilih_menu == '1':
        PeminjamanNonmember()
    elif pilih_menu == '2':
        PengembalianNonMember()
    elif pilih_menu == '3':
        pembelianNonMember()
    elif pilih_menu == '4':
        sys.exit()
    else:
        print("Maaf nomor yang Anda masukkan tidak ada!!")

def login():
    print('\n')
    judul_login = "HALAMAN LOGIN"
    print(judul_login.center(50, '-'))
    nama_plgn = input("Masukkan username Anda = ")
    nik_plgn = input("Masukkan NIK Anda = ")

def register():
    print(50 * "_")
    print("Masukkan data dibawah ini dengan benar!")
    nama_plgnbaru = input("Masukkan username Anda = ")
    nik_plgnbaru = input("Masukkan NIK Anda = ")
    nama_plgn.append(nama_plgnbaru)
    nik_plgn.append(nik_plgnbaru)
    bio_plgn['Tempat lahir'] = input('Tempat lahir = ')
    bio_plgn['Tanggal lahir'] = input('Tanggal lahir (contoh : 11 Januari 2002) = ')
    bio_plgn['Alamat'] = input('Alamat Rumah = ')
    print("Selamat Anda berhasil melakukan registrasi!")
    print(70 * "_")

# Proses login dan register
if awal == "y":
    login()
    print('\n')
    show_menu_member()
    print("Silahkan masukkan data dibawah ini untuk melengkapi langkah peminjaman kaset")
elif awal == "t":
    ask_registrasi = input("Apakah anda ingin melakukan registrasi? (y/t) = ")
    if ask_registrasi == "y":
        register()
        # Memastikan data login dan registrasi
        print("Pastikan data yang anda masukkan sudah benar")
        print("Username = ", nama_plgn)
        print("NIK =", nik_plgn)
        print("Tempat/Tanggal lahir = ", bio_plgn['Tempat lahir'], ',', bio_plgn['Tanggal lahir'])
        print("Alamat = ", bio_plgn['Alamat'])
        cek1 = input("\nApakah data yang anda masukkan sudah benar? (y/t) = ")
        if cek1 == "y":
            login()
            print('\n')
            show_menu_member()
        else:
            register()
    else:
        show_menu_nonmember()
else:
    print()
