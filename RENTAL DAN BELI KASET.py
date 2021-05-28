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
