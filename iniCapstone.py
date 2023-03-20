dataKaryawan = [
    {
        'ID': 'A001',
        'Nama': 'Andi',
        'Gender': 'L',
        'Umur': 26,
        'Posisi': 'Manager F&A'
    },
    {
        'ID': 'B001',
        'Nama': 'Didin',
        'Gender': 'L',
        'Umur': 24,
        'Posisi': 'Manager HRD'
    },
    {
        'ID': 'C001',
        'Nama': 'Tika Amalia',
        'Gender': 'P',
        'Umur': 24,
        'Posisi': 'SPV F&A'
    },
    {
        'ID': 'A002',
        'Nama': 'Amirudin',
        'Gender': 'L',
        'Umur': 26,
        'Posisi': 'Staff F&A'
    },
    {
        'ID': 'B002',
        'Nama': 'Eka Zakia',
        'Gender': 'P',
        'Umur': 24,
        'Posisi': 'Staff HRD'
    }
]

# Menampilkan data karyawan


def data_karyawan():
    print('\n')
    print('Data Karyawan:\n')
    print('=================================================================================')
    print('Index\t| ID\t| Nama    \t| Kelamin\t| Umur\t| Posisi  \t\t|')
    print('---------------------------------------------------------------------------------')
    # enumerate() fungsi yang digunakan untuk mengembalikan panjang iterable dan mengulang itemnya secara bersamaan
    for i, j in enumerate(dataKaryawan):
        print(
            f"{i+1}\t| {j['ID']}\t| {j['Nama']}  \t| {j['Gender']}\t\t| {j['Umur']}\t| {j['Posisi']}  \t\t|")


# Menu Read
def readData():
    while True:
        print('''
    >> Menu Laporan Data Karyawan \n
    1. Laporan Seluruh Data Karyawan
    2. Laporan Data Karyawan Tertentu
    3. Kembali Ke Menu Utama
''')
        subMenu_1 = input('\nPilih Menu [1-3]: ')
        if subMenu_1 == '1':
            data_karyawan()

        elif subMenu_1 == '2':
            if len(dataKaryawan) == 0:  # len() untuk mengembalikan panjang dari suatu objek
                print('\nData Karyawan Kosong')
            elif len(dataKaryawan) != 0:
                ID_Karyawan = input('\nMasukkan ID [4-Digit]: ')

                listID = []
                for i in range(len(dataKaryawan)):

                    listID.append(dataKaryawan[i]['ID'])
                if ID_Karyawan in listID:
                    print(
                        '=================================================================================')
                    print('Index\t| ID\t| Nama\t\t\t| Kelamin\t| Umur\t| Posisi\t|')
                    print(
                        '---------------------------------------------------------------------------------')
                    print(
                        f"{listID.index(ID_Karyawan)}.\t| {ID_Karyawan}\t| {dataKaryawan[listID.index(ID_Karyawan)]['Nama']}\t\t| {dataKaryawan[listID.index(ID_Karyawan)]['Gender']}\t\t| {dataKaryawan[listID.index(ID_Karyawan)]['Umur']}\t| {dataKaryawan[listID.index(ID_Karyawan)]['Posisi']}\t|")
                else:
                    print(
                        f'Data Karyawan dengan ID {ID_Karyawan} tidak tersedia')

        elif subMenu_1 == '3':
            menu_utama()
            break

        else:
            print('Masukkan Angka Yang Benar!')
        close()


# Menu Create
def createData():
    while True:
        print('''
    >> Menu Menambah Data Karyawan \n
    1. Tambah Data Karyawan
    2. Kembali Ke Menu Utama''')
        subMenu_2 = input('\nPilih Menu [1-2]: ')

        if subMenu_2 == '1':
            ID_karyawan_baru = input(
                'Masukkan ID Karyawan (4 Digit Angka): ').upper()
            if len(ID_karyawan_baru) != 4:
                print('ID yang anda input tidak boleh lebih/kurang dari 4 digit!')
            elif len(ID_karyawan_baru) == 4:
                for i in dataKaryawan:
                    if i['ID'] == ID_karyawan_baru:
                        print(f'\nID {ID_karyawan_baru} sudah ada')
                        createData()
                else:
                    Nama_Baru = input('Masukkan Nama: ').capitalize()
                    Gender_Baru = input('Masukkan Gender: ').capitalize()
                    Umur_Baru = input('Masukkan Umur: ')
                    Posisi_Baru = input('Masukkan Posisi: ').capitalize()
                    while True:
                        konfirmasiMenu2 = input(
                            'Yakin untuk menambahkan Data? (Y/N): ').capitalize()
                        if konfirmasiMenu2 == 'Y':
                            data_baru = {'ID': ID_karyawan_baru, 'Nama': Nama_Baru,
                                         'Gender': Gender_Baru, 'Umur': Umur_Baru, 'Posisi': Posisi_Baru}
                            dataKaryawan.append(data_baru)
                            print('\nData Telah Ditambahkan')
                            data_karyawan()
                            break
                        elif konfirmasiMenu2 == 'N':
                            print('\nData Tidak Jadi ditambahkan')
                            # createData()
                        else:
                            print('\nMasukkan Hanya Y/N')
                            createData()
                        break
        elif subMenu_2 == '2':
            menu_utama()
            break
        close()


# Menu update
def updateData():
    while True:
        print('''
    >> Menu Mengubah Data Karyawan \n
    1. Ubah Data Karyawan
    2. Kembali Ke Menu Utama''')
        subMenu_3 = input('\nPilih Menu [1-2]: ')
        if subMenu_3 == '1':
            data_karyawan()
            Input_ID = input('\nMasukkan ID Karyawan: ')
            for i in dataKaryawan:
                if Input_ID == i['ID']:
                    print(
                        '=================================================================================')
                    print('Index\t| ID\t| Nama\t\t\t| Kelamin\t| Umur\t| Posisi\t|')
                    print(
                        '---------------------------------------------------------------------------------')
                    print(
                        f"{i['ID']}\t| {i['Nama']}\t\t\t| {i['Gender']}\t| {i['Umur']}\t| {i['Posisi']}\t|")
                    while True:
                        ubah_kolom = input(
                            'Pilih Kolom Yang Ingin Diubah (ID, Nama, Gender, Umur, Posisi): ').lower()
                        if ubah_kolom == 'id':
                            ubah_kolom = ubah_kolom.upper()
                        else:
                            ubah_kolom = ubah_kolom.capitalize()
                        ubah_isi = input(
                            f'Masukkan {ubah_kolom} baru: ').capitalize()
                        while True:
                            konfirmasi_ubah2 = input(
                                'Apakah Data Jadi Diubah (Y/N)? ').capitalize()
                            if konfirmasi_ubah2 == 'Y':
                                i[ubah_kolom] = ubah_isi
                                print('\nData Sudah Diubah')
                                data_karyawan()
                                break
                            elif konfirmasi_ubah2 == 'N':
                                updateData()
                            else:
                                print('\nMasukkan Y/N Saja!!')
                            updateData()
                            break
                        break
                    break

            else:
                print('\nID tidak tersedia')
                updateData()
                break
        elif subMenu_3 == '2':
            menu_utama()
            break
        close()

# Menu Delete


def deleteData():
    while True:
        print('''
    >> Menu Menghapus Data Karyawan \n
    1. Hapus Data Karyawan
    2. Kembali Ke Menu Utama''')
        subMenu_4 = input('\nPilih Menu [1-2]: ')
        if subMenu_4 == '1':

            if len(dataKaryawan) == 0:
                print('\nData Karyawan Kosong')
            elif len(dataKaryawan) != 0:
                data_karyawan()
                hapus = input('\nMasukkan ID yang mau dihapus: ')
                listID = []
                for i in range(len(dataKaryawan)):
                    listID.append(dataKaryawan[i]['ID'])
                if hapus in listID:
                    print(
                        f'\nYakin Menghapus Data Karyawan Dengan ID "{hapus}"?')
                    konfirmasi = input(
                        'Tekan Y untuk menghapus atau N untuk membatalkan: ').capitalize()
                    if konfirmasi == 'Y':
                        del dataKaryawan[listID.index(hapus)]
                        data_karyawan()
                        print(
                            f'\nData Karyawan Dengan ID {hapus} Telah Dihapus')
                    elif konfirmasi == 'N':
                        print('\nData tidak jadi dihapus')
                    else:
                        print('Masukkan Y/N')
                else:
                    print(f'\nID {hapus} tidak terserdia ')
        elif subMenu_4 == '2':
            menu_utama()
            break
        else:
            close()


# Menu Utama
def menu_utama():
    print('''
=================================================================================
                   Data Karyawan PT. ABC
---------------------------------------------------------------------------------
    1. Laporan Data Karyawan
    2. Menambahkan Data Karyawan
    3. Mengubah Data Karyawan
    4. Menghapus Data Karyawan Karyawan
    5. Exit
''')
    pilihMenu = input('Pilih Menu [1-5]: ')
    if pilihMenu == '1':
        readData()
    elif pilihMenu == '2':
        createData()
    elif pilihMenu == '3':
        updateData()
    elif pilihMenu == '4':
        deleteData()
    elif pilihMenu == '5':
        print('\n"TERIMAKASIH"')
    else:
        menu_utama()
        close()


def close():
    global x
    x = False


x = True
menu_utama()
