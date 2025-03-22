def tulis_angka():
    # Meminta pengguna untuk memasukkan nama file
    nama_file = input('Masukkan nama file yang ingin ditulis: ')

    try:
        # Mencoba membuka file untuk menulis
        outfile = open(nama_file, 'w')
        # Meminta tiga angka dari pengguna
        print('Masukkan tiga angka:')
        angka1 = int(input('Angka #1: '))
        angka2 = int(input('Angka #2: '))
        angka3 = int(input('Angka #3: '))

        # Menulis angka-angka ke dalam file
        outfile.write(str(angka1) + '\n')
        outfile.write(str(angka2) + '\n')
        outfile.write(str(angka3) + '\n')
        print(f"Data angka telah ditulis ke {nama_file}.")
    except ValueError:
        # Menangani kesalahan jika input bukan angka
        print("Input harus berupa angka.")
    except PermissionError:
        # Menangani kesalahan jika izin ditolak
        print(f"Izin untuk menulis ke file '{nama_file}' ditolak.")
    except Exception as e:
        # Menangani kesalahan lain
        print(f"Terjadi kesalahan: {e}")
    else:
        # Menutup file jika tidak ada eksepsi yang terjadi
        outfile.close()
    finally:
        print("Blok finally untuk penulisan dieksekusi.")


def baca_angka():
    # Meminta pengguna untuk memasukkan nama file
    nama_file = input('Masukkan nama file yang ingin dibaca: ')

    try:
        # Mencoba membuka file untuk membaca
        infile = open(nama_file, 'r')
        # Membaca isi file
        angka1 = int(infile.readline().strip())
        angka2 = int(infile.readline().strip())
        angka3 = int(infile.readline().strip())

        # Menutup file
        infile.close()

        # Menghitung jumlah total
        total = angka1 + angka2 + angka3

        # Menampilkan angka-angka dan jumlah totalnya
        print('Angka-angka yang dimasukkan adalah:', angka1, angka2, angka3)
        print('Jumlah totalnya adalah:', total)
    except FileNotFoundError:
        # Menangani kesalahan jika file tidak ditemukan
        print(f"File '{nama_file}' tidak ditemukan.")
    except ValueError:
        # Menangani kesalahan jika isi file bukan angka yang valid
        print("Isi file harus berupa angka yang valid.")
    except PermissionError:
        # Menangani kesalahan jika izin ditolak
        print(f"Izin untuk membuka file '{nama_file}' ditolak.")
    except Exception as e:
        # Menangani kesalahan lain
        print(f"Terjadi kesalahan: {e}")
    finally:
        print("Blok finally untuk pembacaan dieksekusi.")

# Memanggil fungsi tulis_angka dan baca_angka
tulis_angka()
baca_angka()