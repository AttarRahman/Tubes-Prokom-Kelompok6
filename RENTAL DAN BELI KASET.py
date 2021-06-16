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
