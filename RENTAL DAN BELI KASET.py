#PROGRAM PENYEWAAN DAN PEMBELIAN KASET
Judul_Program = "PROGRAM SEWA & BELI KASET"
print(70*"=")
print(Judul_Program.center(70))
print(70*"=")
awal = input("Apakah anda member? (y/t) = ")
nama_plgn = []
nik_plgn = []
bio_plgn = {}
bio_kaset = {}
jaminan = {}
def Tabel_hargasewa():
    No = [1, 2, 3, 4, 5]
    Genre_film = ['Thriller', 'Comedy', 'Romance', 'Action', 'Drama']
    Kode_film = ['A', 'B', 'C', 'D', 'E']
    Harga_sewa = [8000, 6000, 6000, 7000, 5000]
    print('''
    __________________________________________________
    | No |   Genre Film   |  Kode Film  | Harga Sewa |
    --------------------------------------------------''')
    for x in range(len(No)):
        isi = str(No[x])
        print('    |   '+isi, end='')
        for y in range(3-6-len(isi)):
            print(' ', end='')
        isi1 = str(Genre_film[x])
        print('| '+isi1, end='')
        for y in range(20-5-len(isi1)):
            print(' ', end='')
        isi2 = str(Kode_film[x])
        print('|            '+isi2, end='')
        for y in range(20-3-len(isi2)):
            print('', end='')
        isi3 = str(Harga_sewa[x])
        print('|        ' + isi3, end='')
        for y in range(20-5-len(isi3)):
            print('', end='')
        print('|')
    print('''
    --------------------------------------------------''')
def Formulir_sewa():
    Tabel_hargasewa()
    bio_kaset['Nama kaset'] = input('Masukkan nama kaset Anda = ')
    bio_kaset['Kode Kaset'] = input('Masukkan kode kaset Anda = ')
    bio_kaset['Genre kaset'] = input('Masukkan genre kaset Anda = ')
    bio_kaset['Nomor telefon'] = input('Masukkan nomor telefon Anda = ')
    jaminan['Nomor telefon'] = input('Masukkan nomor telefon Anda = ')
    nik_plgnsewa = input("Masukkan NIK Anda = ")
    nik_plgn.append(nik_plgnsewa)
    bio_plgn['Alamat'] = input('Alamat Rumah')

def Peminjaman():
    Formulir_sewa()
    # Mamastikan data login dan registrasi
    print("Pastikan data yang anda masukkan sudah benar")
    print("Name kaset = ",bio_kaset['Nama kaset'])
    print("Kode Kaset = ",bio_kaset['Kode kaset'])
    print("Genre Kaset = ", bio_kaset['Nomor telefon'])
    print("No.Telepon = ", jaminan['Nomor telefon'])
    print("NIK = ", nik_plgn)
    print("Alamat = ",bio_plgn['Alamat'])

    # Akumulasi tanggal pinjam dan tanggal pengembalian
    from datetime import timedelta,datetime
    tanggal_pinjam = datetime.today()
    tanggal_kembali = tanggal_pinjam + timedelta(days=7)
    print(tanggal_pinjam.strftime("Tanggal Peminjaman = %d/%m/%Y, %H:%M:%S"))
    print(tanggal_kembali.strftime("Tanggal Kembali = %d/%m/%Y, %H:%M:%S"))

    cek2 = input("\nApakah data yang anda masuukan sudah benar ? (y/t) = ")
    if cek2 == "y":
        """akan lanjut ke daf HitungHargaSewa yang isisnya perhitungan harga sewa tapi belum di bikin"""
    else:
        """Kalo salah akan kembali ke input formulir sewa"""
        Formulir_sewa()

def HitungHargaSewa():
    print()

def Pengembalian():
    print("untuk program pengembalian kaset")

def Pembelian():
    print()

def show_menu():
    import sys
    print("\n")
    judul_menu = "Pilih Menu"
    print(judul_menu.center(70, '-'))
    print("[1]  Peminjaman Kaset")
    print("[2]  Pengembalian Kaset")
    print("[3]  Pembelian Kaset")
    print("[4]  Keluar")
    pilih_menu = input("Pilih menu --> ")
    print("\n")

    if pilih_menu == '1':
        Peminjaman()
    elif pilih_menu == '2':
        print("Belum jadi")    
    elif pilih_menu == '3':
        print("Belum jadi")
    elif pilih_menu == '4':
        sys.exit()
    else:
        print("Maaf nomor yang Anda masukkan tidak ada!!")
        
def login():
    print('\n')
    judul_login = "HALAMAN LOGIN"
    print(judul_login.center(70, '-'))
    nama_plgn = input("Masukkan username Anda = ")
    nik_plgn = input("Masukkan NIK Anda = ")

def register():
    print(70 * "_")
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
    # fungsi login
    """ ini yg blm register bisa lolos. jadi harus dibikin fungsi biar dia nolakyg blm punya member"""


    login()
    print('\n')
    show_menu()
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
        else:
            register()
    else:
        print("Ulangi mengisi formulir sewa")
        show_menu()
else:
    print()    
