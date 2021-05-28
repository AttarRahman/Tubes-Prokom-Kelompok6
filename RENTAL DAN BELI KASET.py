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


