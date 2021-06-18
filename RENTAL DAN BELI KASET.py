# PROGRAM PENYEWAAN DAN PEMBELIAN KASET
import sys
import time
import datetime
import random
# Random nomor kartu peminjaman
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
batas_pinjam = []
tanggal_pinjam = {}
harga = []
totalharga = []
diskon = []
genre_kaset = []
jumlahpesan = []
menu = []
denda = []
Genre_kaset = []
que1 = []
que2 = []
date0 = 0
date1 = 0
date2 = 0


def halamanutama():
    #menampilkan header
    judulprogram1 = "PROGRAM SEWA & BELI KASET"
    judulprogram2 = "TOKO INDENTURE DISC"
    print(50 * "=")
    print(judulprogram1.center(50))
    print(judulprogram2.center(50))
    print(50 * "=")


def login():
    #menampilkan halaman login dan menginput data login
    global nama_plgn, nik_plgn
    print('\n')
    jdl_login = "####   Login Member   ####"
    print(jdl_login.center(50))
    nama_plgn = input("Nama member = ")
    nik_plgn = input("NIK         = ")
    print(50 * "-")


def registrasi():
    #menampilkan dan menginput data registrasi
    global nama_plgn, nik_plgn, tempat_lahir, tanggal_lahir, nomor_telefon, alamat
    if que2 == "Y" or que2 == "y":
        jdl_reg = "####   Registrasi Member   ####"
        print("\n", jdl_reg.center(50))
        nama_plgn = input("Masukkan nama Anda = ")
        nik_plgn = input("Masukkan NIK Anda = ")
        tempat_lahir = input("Tempat lahir = ")
        tanggal_lahir = input("Tanggal lahir (contoh : 11 Januari 2002) = ")
        nomor_telefon = input("Masukkan nomor telefon Anda = ")
        alamat = input("Alamat Rumah = ")
        #memastikan data yang dimasukkan sudah benar
        print(50 * "=")
        print("Pastikan data yang anda masukkan sudah benar.\n")
        print("Nama = ", nama_plgn)
        print("NIK = ", nik_plgn)
        print("Tempat/Tanggal lahir = ", tempat_lahir, ",", tanggal_lahir)
        print("Nomor telefon = ", nomor_telefon)
        print("Alamat = ", alamat)
        print(50 * "_")
        #menyimpan data kedalam database
        biodata = """\nNama = {}\nNIK = {}\nTempat/Tanggal lahir = {}\nNomor Telefon = {}
Alamat = {}\n""".format(nama_plgn, nik_plgn, tempat_lahir + "," + tanggal_lahir, nomor_telefon, alamat)
        database = open("databasemember.txt", "a")
        database.write(biodata)
        database.close()
    else:
        pass


def show_menu_nonmember():
    #menampilkan pilihan menu utama untuk non member
    print("\n")
    judul_menu = "Pilih Menu"
    print(judul_menu.center(50, '-'))
    print("""
    [1]  Peminjaman Kaset
    [2]  Pengembalian Kaset
    [3]  Pembelian Kaset
    [4]  Keluar""")
    print(50 * "-")
    pilih_menu = input("Pilih menu --> ")
    print("\n")
    if pilih_menu == '1':
        peminjaman_nonmember()
    elif pilih_menu == '2':
        pengembalian_nonmember()
    elif pilih_menu == '3':
        pembelian()
    elif pilih_menu == '4':
        halamanutama()
        sys.exit()
    else:
        print("Maaf nomor yang Anda masukkan tidak ada!!")


def show_menu_member():
    # menampilkan pilihan menu utama untuk member
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
        peminjaman_member()
    elif pilih_menu == '2':
        pengembalian_member()
    elif pilih_menu == '3':
        pembelian()
    elif pilih_menu == '4':
        halamanutama()
        sys.exit()
    else:
        print("Maaf nomor yang Anda masukkan tidak ada!!")


def tabel_hargasewa():
    # menampilkan tabel harga sewa kaset
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


def formulirsewa_member():
    # menginput data formulir peminjaman kaset  untuk member
    global jaminan, bio_kaset
    print("\nSilahkan masukkan data dibawah ini untuk melengkapi langkah peminjaman kaset")
    bio_kaset['Nama kaset'] = input('\nMasukkan nama kaset Anda    = ')
    bio_kaset['Kode kaset'] = input('Masukkan kode kaset Anda    = ')
    bio_kaset['Genre kaset'] = input('Masukkan genre kaset Anda   = ')
    bio_kaset['Jumlah kaset'] = int(input('Masukkan jumlah kaset       = '))
    jaminan = input('Masukkan nomor telefon Anda = ')


def formulirsewa_nonmember():
    # menginput data formulir peminjaman kaset  untuk non member
    global alamat, bio_kaset, jaminan
    print("Silahkan masukkan data dibawah ini untuk melengkapi langkah peminjaman kaset")
    bio_kaset['Nama kaset'] = input('\nMasukkan nama kaset Anda    = ')
    bio_kaset['Kode kaset'] = input('Masukkan kode kaset Anda    = ')
    bio_kaset['Genre kaset'] = input('Masukkan genre kaset Anda   = ')
    bio_kaset['Jumlah kaset'] = int(input('Masukkan jumlah kaset       = '))
    jaminan = input('Masukkan nomor telefon Anda = ')
    nik_nonmember = input("Masukkan NIK Anda           = ")
    nik_plgn.append(nik_nonmember)
    alamat = input('Alamat Rumah                = ')


def peminjaman_member():
    global date1, date2, date0, tanggal_pinjam, batas_pinjam
    #menampilkan tabel dan formulir peminjaman kaset
    tabel_hargasewa()
    formulirsewa_member()
    #memastikan data formulir peminjaman kaset
    print("\nPastikan data yang anda masukkan sudah benar")
    print("Name kaset   = ", bio_kaset['Nama kaset'])
    print("Jumlah kaset = ", bio_kaset['Jumlah kaset'])
    print("Kode kaset   = ", bio_kaset['Kode kaset'])
    print("Genre kaset  = ", bio_kaset['Genre kaset'])
    print("No.Telepon   = ", jaminan)
    print("NIK          = ", nik_plgn)
    print("Alamat       = ", alamat)
    #akumulasi tanggal pinjam dan tanggal pengembalian
    tanggal_pinjam = input('Tanggal mulai peminjaman kaset (YYYY-MM-DD) = ')
    year, month, day = map(int, tanggal_pinjam.split('-'))
    date0 = datetime.datetime(year, month, day)
    batas_pinjam = input('Batas pengembalian kaset (YYYY-MM-DD) = ')
    year, month, day = map(int, batas_pinjam.split('-'))
    date1 = datetime.datetime(year, month, day)
    date2 = datetime.datetime(year, month, day)
    print("Tanggal pinjam            = ", tanggal_pinjam)
    print("Tangal Batas Pengembalian =", batas_pinjam)
    #menampilkan kartu peminjaman kaset
    ques1 = input("\nApakah data yang anda masukan sudah benar ? (y/t) = ")
    print()
    if ques1.upper() == "Y":
        print("""
______________________________________________________________
|               KARTU PEMINJAMAN INDENTURE DISC              |
|                 Jln.Gagak No.15, Surakarta                 |
--------------------------------------------------------------
                """)
        isikartu_peminjaman_dan_pengembalian()
        ques2 = input("Apakah Anda ingin melanjutkan transaksi pembayaran? (y/t) = ")
        if ques2.upper() == "Y":
            struk_peminjaman_pengembalian_member()
            ques3 = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
            if ques3.upper() == "Y":
                show_menu_member()
        else:
            halamanutama()
            sys.exit()
    else:
        peminjaman_member()


def peminjaman_nonmember():
    global date0, date1, date2, tanggal_pinjam, batas_pinjam
    # menampilkan tabel dan formulir peminjaman kaset
    tabel_hargasewa()
    formulirsewa_nonmember()
    #memastikan data formulir peminjaman kaset
    print("\nPastikan data yang anda masukkan sudah benar")
    print("Name kaset   = ", bio_kaset['Nama kaset'])
    print("Jumlah kaset = ", bio_kaset['Jumlah kaset'])
    print("Kode kaset   = ", bio_kaset['Kode kaset'])
    print("Genre kaset  = ", bio_kaset['Genre kaset'])
    print("No.Telepon   = ", jaminan)
    print("NIK          = ", nik_plgn)
    print("Alamat       = ", alamat)
    #akumulasi tanggal pinjam dan tanggal pengembalian
    tanggal_pinjam = input('Tanggal mulai peminjaman kaset (YYYY-MM-DD) = ')
    year, month, day = map(int, tanggal_pinjam.split('-'))
    date0 = datetime.datetime(year, month, day)
    batas_pinjam = input('Batas pengembalian kaset (YYYY-MM-DD) = ')
    year, month, day = map(int, batas_pinjam.split('-'))
    date1 = datetime.datetime(year, month, day)
    date2 = datetime.datetime(year, month, day)
    print("Tanggal pinjam            = ", tanggal_pinjam)
    print("Tangal Batas Pengembalian =", batas_pinjam)
    #menampilkan kartu peminjaman kaset
    ques1 = input("\nApakah data yang Anda masukkan sudah benar ? (y/t) = ")
    print()
    if ques1.upper() == "Y":
        print("""
______________________________________________________________
|               KARTU PEMINJAMAN INDENTURE DISC              |
|                 Jln.Gagak No.15, Surakarta                 |
--------------------------------------------------------------
                """)
        isikartu_peminjaman_dan_pengembalian()
        ques2 = input("Apakah Anda ingin melanjutkan transaksi pembayaran? (y/t) = ")
        if ques2.upper() == "Y":
            struk_peminjaman_pembelian_nonmember()
            ques3 = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
            if ques3.upper() == "Y":
                show_menu_nonmember()
        else:
            sys.exit()
    else:
        peminjaman_nonmember()


def struk_peminjaman_pengembalian_member():
    global harga, date2, diskon, denda, genre_kaset, nomor_kartupeminjaman, totalharga, jumlahpesan, menu
    #perhitungan biaya peminjaman dan pengembalian kaset member
    kode_kaset = bio_kaset['Kode kaset']
    jumlahpesan = bio_kaset['Jumlah kaset']
    if kode_kaset == "A":
        #Genre Kaset = 'Thriller'
        genre_kaset = 'Thriller'
        harga = int((8000 * jumlahpesan)/2)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "B":
        #Genre kaset = 'Comedy'
        genre_kaset = 'Comedy'
        harga = int((6000 * jumlahpesan)/2)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "C":
        #Genre kaset = 'Romance'
        genre_kaset = 'Romance'
        harga = int((6000 * jumlahpesan)/2)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "D":
        #Genre kaset = 'Action'
        genre_kaset = 'Action'
        harga = int((7000 * jumlahpesan)/2)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "E":
        #Genre kaset = 'Drama'
        genre_kaset = 'Drama'
        harga = int((5000 * jumlahpesan)/2)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    else:
        genre_kaset = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
    #menampilkan pilihan metode pembayaran
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
    selisih = date2 - date1
    sel = str(selisih)
    jumlah = sel[0:1]
    denda = 500 * int(jumlah)
    if menupembayaran.upper() == "A":
        print("""
Untuk peminjaman total harga yang dibayarkan merupakan 50% 
dari harga sewa, pelunasan akan dilakukan setelah kaset dikembalikan.
             """)
        print("Total harga yang harus Anda bayarkan = Rp", totalharga+denda)
        bayar = int(input("Masukkan uang tunai Anda             = Rp"))
        #metode pembayaran = Tunai
        print("\n")
        print("="*45)
        nama = "STRUK PEMBAYARAN"
        nama2 = "INDENTURE DISC"
        print(nama.center(45))
        print(nama2.center(45))
        print("=" * 45)
        print("\nPeminjaman Kaset :")
        print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
        print("-"*45)
        print("Total Harga (50% pembayaran)     ", harga)
        print("Jumlah denda Anda adalah           %s" % denda)
        print("Diskon 10%                       ", diskon)
        print("                          -----------------")
        print("Total Bayar                      ", totalharga+denda)
        print("Tunai                            ", bayar)
        print("Kembalian                        ", bayar - totalharga-denda)
        print("Kode Peminjaman                  ", nomor_kartupeminjaman)
        print("-"*45)
        print("\n===========Terimakasih,Selamat Datang Kembali============")
    else:
        #metode pembayaran = Ovo,Transfer, dan Dana
        print("""
Untuk peminjaman total harga yang dibayarkan merupakan 50% 
dari harga sewa, pelunasan akan dilakukan setelah kaset dikembalikan.
                     """)
        print("Total harga yang harus Anda bayarkan = Rp", totalharga+denda)
        print(""" 
        ____________________________________________________
        | Note:                                            |
        | 1. Ovo          = 085555666777 (a.n Bagus S)     |
        | 2. Mbanking(BCA)= 20210002901 (a.n Cristin A)    |
        | 3. Dana         = 089111222334 (a.n Erika N S    | 
        ----------------------------------------------------
               """)
        cara = int(input("Pilih >>> "))
        if cara == 1:
            menu = 'OVO payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            #jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Jumlah denda Anda adalah           %s" % denda)
            print("Diskon 10%                       ", diskon)
            print("                          ------------------")
            print("Total Bayar                      ", totalharga+denda)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        elif cara == 2:
            menu = 'Mbanking payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Jumlah denda Anda adalah           %s" % denda)
            print("Diskon 10%                       ", diskon)
            print("                          ------------------")
            print("Total Bayar                      ", totalharga+denda)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        elif cara == 3:
            menu = 'Dana payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Jumlah denda Anda adalah           %s" % denda)
            print("Diskon 10%                       ", diskon)
            print("                          ------------------")
            print("Total Bayar                      ", totalharga+denda)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        else:
            pass


def struk_peminjaman_pembelian_nonmember():
    global harga, diskon, denda, genre_kaset, nomor_kartupeminjaman, totalharga, jumlahpesan, menu
    kode_kaset = bio_kaset['Kode kaset']
    jumlahpesan = bio_kaset['Jumlah kaset']
    if kode_kaset == "A":
        # Genre Kaset = 'Thriller'
        genre_kaset = 'Thriller'
        harga = int((8000 * jumlahpesan) / 2)
        diskon = 0
        totalharga = int(harga - diskon)
    elif kode_kaset == "B":
        # Genre kaset = 'Comedy'
        genre_kaset = 'Comedy'
        harga = int((6000 * jumlahpesan) / 2)
        diskon = 0
        totalharga = int(harga - diskon)
    elif kode_kaset == "C":
        # Genre kaset = 'Romance'
        genre_kaset = 'Romance'
        harga = int((6000 * jumlahpesan) / 2)
        diskon = 0
        totalharga = int(harga - diskon)
    elif kode_kaset == "D":
        # Genre kaset = 'Action'
        genre_kaset = 'Action'
        harga = int((7000 * jumlahpesan) / 2)
        diskon = 0
        totalharga = int(harga - diskon)
    elif kode_kaset == "E":
        # Genre kaset = 'Drama'
        genre_kaset = 'Drama'
        harga = int((5000 * jumlahpesan) / 2)
        diskon = 0
        totalharga = int(harga - diskon)
    else:
        genre_kaset = "-"
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
    selisih = date2 - date1
    sel = str(selisih)
    jumlah = sel[0:1]
    denda = 500 * int(jumlah)
    if menupembayaran.upper() == "A":
        print("""
Untuk peminjaman total harga yang dibayarkan merupakan 50% 
dari harga sewa, pelunasan akan dilakukan setelah pengembalian kaset.
                 """)
        print("Total harga yang harus Anda bayarkan = Rp", totalharga+denda)
        bayar = int(input("Masukkan uang tunai Anda             = Rp "))
        # print("Tunai")
        print("\n")
        print("=" * 45)
        nama = "STRUK PEMBAYARAN"
        nama2 = "INDENTURE DISC"
        print(nama.center(45))
        print(nama2.center(45))
        print("=" * 45)
        print("\nPeminjaman Kaset :")
        print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
        print("-" * 45)
        print("Total Harga (50% pembayaran)     ", harga)
        print("Jumlah denda Anda adalah           %s" % denda)
        print("Diskon                           ", diskon)
        print("                          -----------------")
        print("Total Bayar                      ", totalharga + denda)
        print("Tunai                            ", bayar)
        print("Kembalian                        ", bayar - totalharga - denda)
        print("Kode Peminjaman                  ", nomor_kartupeminjaman)
        print("-" * 45)
        print("\n===========Terimakasih,Selamat Datang Kembali============")
    else:
        # Melalui Ovo,Transfer, dan Dana
        print("""
Untuk peminjaman total harga yang dibayarkan merupakan 50% 
dari harga sewa, pelunasan akan dilakukan setelah pengembalian kaset.
                         """)
        print("Total harga yang harus Anda bayarkan = Rp", totalharga+denda)
        print(""" 
            ____________________________________________________
            | Note:                                            |
            | 1. Ovo          = 085555666777 (a.n Bagus S)     |
            | 2. Mbanking(BCA)= 20210002901 (a.n Cristin A)    |
            | 3. Dana         = 089111222334 (a.n Erika N S    | 
            ----------------------------------------------------
                   """)
        cara = int(input("Pilih >>> "))
        if cara == 1:
            menu = 'OVO payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Jumlah denda Anda adalah           %s" % denda)
            print("Diskon                           ", diskon)
            print("                          -----------------")
            print("Total Bayar                      ", totalharga+denda)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        elif cara == 2:
            menu = 'Mbanking payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Jumlah denda Anda adalah           %s" % denda)
            print("Diskon                           ", diskon)
            print("                          -----------------")
            print("Total Bayar                      ", totalharga+denda)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        elif cara == 3:
            menu = 'Dana payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Jumlah denda Anda adalah           %s" % denda)
            print("Diskon                           ", diskon)
            print("                          -----------------")
            print("Total Bayar                      ", totalharga+denda)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        else:
            pass


def isikartu_peminjaman_dan_pengembalian():
    print("  Nomor Nota                = ", nomor_kartupeminjaman)
    print("  NIK                       = ", nik_plgn)
    print("  Alamat                    = ", alamat)
    print("  Nama Kaset                = ", bio_kaset['Nama kaset'])
    print("  Kode Kaset                = ", bio_kaset['Kode kaset'])
    print("  Genre Kaset               = ", bio_kaset['Genre kaset'])
    print("  Tanggal pinjam            = ", tanggal_pinjam)
    print("  Tangal Batas Pengembalian =", batas_pinjam)


def pengembalian_member():
    global date2, nomor_kartupeminjaman
    # menginput nomor kartu peminjaman member
    nomor_kartupeminjaman = input("Masukkan nomor kartu peminjaman Anda = ")
    print("Apakah benar %s nomor kartu peminjaman Anda? (y/t)" % nomor_kartupeminjaman)
    cek = input(">>> ")
    # menampilkan kartu pengembalian member
    if cek.upper() == "Y":
        tanggal_kembali = input('Tanggal Anda mengembalikan kaset YYYY-MM-DD format = ')
        year, month, day = map(int, tanggal_kembali.split('-'))
        date2 = datetime.datetime(year, month, day)
        print("""
______________________________________________________________
|              KARTU PENGEMBALIAN INDENTURE DISC             |
|                 Jln.Gagak No.15, Surakarta                 |
--------------------------------------------------------------
                """)

        isikartu_peminjaman_dan_pengembalian()
        cek1 = input("Apakah Anda ingin melanjutkan transaksi pembayaran? (y/t) = ")
        if cek1.upper() == "Y":
            struk_peminjaman_pengembalian_member()
            cek2 = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
            if cek2.upper() == "Y":
                show_menu_member()
        else:
            sys.exit()
    else:
        pengembalian_member()


def pengembalian_nonmember():
    global date2, nomor_kartupeminjaman
    # menginput nomor kartu peminjaman nonmember
    nomor_kartupeminjaman = input("Masukkan nomor kartu peminjaman Anda = ")
    print("Apakah benar %s nomor kartu peminjaman Anda? (y/t)" % nomor_kartupeminjaman)
    cek = input(">>> ")
    # menampilkan kartu pengembalian nonmember
    if cek.upper() == "Y":
        tanggal_kembali = input('Tanggal Anda mengembalikan kaset YYYY-MM-DD format = ')
        year, month, day = map(int, tanggal_kembali.split('-'))
        date2 = datetime.datetime(year, month, day)
        print("""
______________________________________________________________
|              KARTU PENGEMBALIAN INDENTURE DISC             |
|                 Jln.Gagak No.15, Surakarta                 |
--------------------------------------------------------------
                """)
        isikartu_peminjaman_dan_pengembalian()
        cek1 = input("Apakah Anda ingin melanjutkan transaksi pembayaran? (y/t) = ")
        if cek1.upper() == "Y":
            struk_peminjaman_pembelian_nonmember()
            cek2 = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
            if cek2.upper() == "Y":
                show_menu_nonmember()
        else:
            sys.exit()


def tabel_hargabeli():
    # menampilkan tabel harga beli kaset
    print('''
    ___________________________________________________
    |  No |   Genre Film   |  Kode Film  | Harga Beli |
    ---------------------------------------------------
    |  1. |  Thriller      |      A      |   15000    | 
    |  2. |  Comedy        |      B      |   13000    |
    |  3. |  Romance       |      C      |   13000    |
    |  4. |  Action        |      D      |   17000    |
    |  5. |  Drama         |      E      |   15000    |
    --------------------------------------------------- ''')


def pembelian():
    global jumlahpesan, genre_kaset, harga, diskon, totalharga, menu
    # menginput data formulir pembelian kaset
    print("""Diskon Alert !!!
Untuk para pelanggan setia Toko Indenture Disc, ada promo diskon 10% 
untuk pembelian kaset semua genre yang ada di Toko Indenture Disc. 
Diskon berlaku untuk member maupun nonmember ~~~""")
    tabel_hargabeli()
    print("Silahkan masukkan data dibawah ini untuk melengkapi langkah pembelian kaset")
    bio_kaset['Nama kaset'] = input('\nMasukkan nama kaset Anda = ')
    bio_kaset['Kode kaset'] = input('Masukkan kode kaset Anda = ')
    bio_kaset['Genre kaset'] = input('Masukkan genre kaset Anda = ')
    bio_kaset['Jumlah kaset'] = int(input('Masukkan jumlah kaset = '))
    # perhitungan biaya pembelian kaset
    kode_kaset = bio_kaset['Kode kaset']
    jumlahpesan = bio_kaset['Jumlah kaset']
    if kode_kaset == "A":
        # Genre Kaset = 'Thriller'
        genre_kaset = 'Thriller'
        harga = (15000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "B":
        # Genre kaset = 'Comedy'
        genre_kaset = 'Comedy'
        harga = (13000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "C":
        # Genre kaset = 'Romance'
        genre_kaset = 'Romance'
        harga = (13000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "D":
        # Genre kaset = 'Action'
        genre_kaset = 'Action'
        harga = (17000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    elif kode_kaset == "E":
        # Genre kaset = 'Drama'
        genre_kaset = 'Drama'
        harga = (15000 * jumlahpesan)
        diskon = int(harga * 0.1)
        totalharga = int(harga - diskon)
    else:
        genre_kaset = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
    # menampilkan pilihan metode pembayaran
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
        # print("Tunai")
        print("Total harga yang harus Anda bayarkan = Rp", totalharga)
        bayar = int(input("Masukkan uang tunai Anda             = Rp "))
        print("\n")
        print("=" * 45)
        nama = "STRUK PEMBAYARAN"
        nama2 = "INDENTURE DISC"
        print(nama.center(45, "="))
        print(nama2.center(45))
        print("=" * 45)
        print("\nPembelian Kaset :")
        print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
        print("-" * 45)
        print("Total Harga                      ", harga)
        print("Diskon 10%                       ", diskon)
        print("                          -----------------")
        print("Total Bayar                      ", totalharga)
        print("Tunai                            ", bayar)
        print("Kembalian                        ", bayar - totalharga)
        print("-" * 45)
        print("\n=========Terimakasih,Selamat Datang Kembali==========")
        cek1 = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
        if cek1.upper() == "Y":
            show_menu_nonmember()
        else:
            sys.exit()
    else:
        # metode pembayaran = Ovo,Transfer, dan Dana
        print("Total harga yang harus Anda bayarkan = Rp", totalharga)
        print(""" 
                    ____________________________________________________
                    | Note:                                            |
                    | 1. Ovo          = 085555666777 (a.n Bagus S)     |
                    | 2. Mbanking(BCA)= 20210002901 (a.n Cristin A)    |
                    | 3. Dana         = 089111222334 (a.n Erika N S    | 
                    ----------------------------------------------------
                           """)
        cara = int(input("Pilih >>> "))
        if cara == 1:
            menu = 'OVO payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPembelian Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Diskon                           ", diskon)
            print("                          -----------------")
            print("Total Bayar                      ", totalharga)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        elif cara == 2:
            menu = 'Mbanking payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Diskon                           ", diskon)
            print("                          -----------------")
            print("Total Bayar                      ", totalharga)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        elif cara == 3:
            menu = 'Dana payment'
            print("""
Batas waktu pembayaran Anda 10 menit, silahkan melakukan transaksi segera.""")
            print("\nMenunggu proses pembayaran...")
            # jeda 10 detik
            time.sleep(10)
            print("Pembayaran Berhasil")
            print("\n")
            print("=" * 45)
            nama = "STRUK PEMBAYARAN"
            nama2 = "INDENTURE DISC"
            print(nama.center(45))
            print(nama2.center(45))
            print("=" * 45)
            print("\nPeminjaman Kaset :")
            print(bio_kaset['Nama kaset'], "(%s)" % genre_kaset, "x", jumlahpesan, "    ", harga)
            print("-" * 45)
            print("Total Harga (50% pembayaran)     ", harga)
            print("Diskon                           ", diskon)
            print("                          -----------------")
            print("Total Bayar                      ", totalharga)
            print("Menu Pembayaran    :", menu)
            print("Kode Peminjaman                  ", nomor_kartupeminjaman)
            print("-" * 45)
            print("\n===========Terimakasih,Selamat Datang Kembali============")
        else:
            pass
        # memastikan apakah masih terdapat transaksi yang ingin dilakukan
        cek1 = input("Apakah Anda ingin melakukan transaksi lainnya? (y/t) = ")
        if cek1.upper() == "Y":
            show_menu_member()
        else:
            sys.exit()


def akses_masuk():
    halamanutama()
    global que1, que2
    que1 = input("Apakah anda member? (y/t) = ")
    # Proses login dan register
    if que1.upper() == "Y":
        login()
        show_menu_member()
    elif que1.upper() == "T":
        que2 = input("Apakah anda ingin melakukan registrasi? (y/t) = ")
        registrasi()
        que3 = input("\nApakah data yang anda masukkan sudah benar? (y/t) = ")
        if que3.upper() == "Y":
            correct = "Registrasi Berhasil"
            print(correct.center(50, "="))
            print('\n')
            akses_masuk()
        else:
            print("Masukkan data yang benar!")
            registrasi()
            print(50 * "_")
    else:
        #jalur nonmember
        print("Maaf pilihan yang Anda masukkan salah")
        print("Anda masuk program sebagai non member")
        show_menu_nonmember()


akses_masuk()
