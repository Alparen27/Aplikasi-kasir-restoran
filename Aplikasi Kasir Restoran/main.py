
from makanan import Makanan
from minuman import Minuman
from pelanggan import Pelanggan
from transaksi import Transaksi


# List untuk menyimpan data
daftar_menu = []
daftar_pelanggan = []
daftar_transaksi = []


# Fungsi mencari menu berdasarkan ID
def cari_menu(id_menu):
    for menu in daftar_menu:
        if menu.get_id_menu() == id_menu:
            return menu
    return None


# Fungsi mencari pelanggan berdasarkan ID
def cari_pelanggan(id_pelanggan):
    for pelanggan in daftar_pelanggan:
        if pelanggan.get_id() == id_pelanggan:
            return pelanggan
    return None


# Fungsi menambahkan data menu
def tambah_menu():
    print("\n=== TAMBAH MENU ===")
    print("1. Makanan")
    print("2. Minuman")

    jenis = input("Pilih jenis menu: ")

    if jenis not in ["1", "2"]:
        print("Pilihan tidak valid!")
        return

    id_menu = input("ID Menu: ").strip()

    if not id_menu:
        print("ID menu tidak boleh kosong!")
        return

    if cari_menu(id_menu):
        print("ID menu sudah digunakan!")
        return

    nama = input("Nama Menu: ").strip()

    if not nama:
        print("Nama menu tidak boleh kosong!")
        return

    try:
        harga = int(input("Harga: Rp"))
        if harga <= 0:
            print("Harga harus lebih dari 0!")
            return
    except ValueError:
        print("Harga harus berupa angka!")
        return

    if jenis == "1":
        jenis_makanan = input("Jenis makanan: ")
        level = input("Level pedas: ")

        menu = Makanan(
            id_menu, nama, harga,
            jenis_makanan, level
        )

    else:
        ukuran = input("Ukuran minuman: ")
        suhu = input("Suhu minuman: ")

        menu = Minuman(
            id_menu, nama, harga,
            ukuran, suhu
        )

    daftar_menu.append(menu)
    print("Menu berhasil ditambahkan!")


# Fungsi menampilkan semua menu
def tampilkan_menu():
    print("\n=== DAFTAR MENU RESTORAN ===")

    if not daftar_menu:
        print("Belum ada data menu.")
        return

    for menu in daftar_menu:
        print("----------------------")
        menu.tampilkan_info()


# Fungsi mencari data menu
def cari_data():
    print("\n=== CARI MENU ===")
    id_menu = input("Masukkan ID Menu: ").strip()

    menu = cari_menu(id_menu)

    if menu:
        print("Menu ditemukan!")
        menu.tampilkan_info()
    else:
        print("Menu tidak ditemukan!")


# Fungsi mengubah data menu
def ubah_data():
    print("\n=== UBAH MENU ===")
    id_menu = input("Masukkan ID Menu: ").strip()

    menu = cari_menu(id_menu)

    if menu is None:
        print("Menu tidak ditemukan!")
        return

    print("1. Ubah harga")
    print("2. Ubah status")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        try:
            harga = int(input("Harga baru: Rp"))

            if harga <= 0:
                print("Harga harus lebih dari 0!")
                return

            menu.ubah_harga(harga)
            print("Harga berhasil diubah!")

        except ValueError:
            print("Harga harus berupa angka!")

    elif pilihan == "2":
        print("1. Tersedia")
        print("2. Habis")

        status = input("Pilih status: ")

        if status == "1":
            menu.ubah_status("Tersedia")
        elif status == "2":
            menu.ubah_status("Habis")
        else:
            print("Pilihan tidak valid!")
            return

        print("Status berhasil diubah!")

    else:
        print("Pilihan tidak valid!")


# Fungsi cek status menu
def cek_status():
    print("\n=== CEK STATUS MENU ===")
    id_menu = input("Masukkan ID Menu: ").strip()

    menu = cari_menu(id_menu)

    if menu:
        print("Nama   :", menu.get_nama())
        print("Status :", menu.get_status())
    else:
        print("Menu tidak ditemukan!")


# Fungsi menambahkan pelanggan
def tambah_pelanggan():
    print("\n=== TAMBAH PELANGGAN ===")

    id_pelanggan = input("ID Pelanggan: ").strip()

    if not id_pelanggan:
        print("ID pelanggan tidak boleh kosong!")
        return

    if cari_pelanggan(id_pelanggan):
        print("ID pelanggan sudah digunakan!")
        return

    nama = input("Nama Pelanggan: ").strip()
    metode_pembayaran = input("Metode Pembayaran: ").strip()

    if not nama or not metode_pembayaran:
        print("Nama dan metode pembayaran tidak boleh kosong!")
        return

    pelanggan = Pelanggan(
        id_pelanggan, nama, metode_pembayaran
    )

    daftar_pelanggan.append(pelanggan)

    print("Pelanggan berhasil ditambahkan!")


# Fungsi membuat transaksi
def tambah_transaksi():
    print("\n=== TRANSAKSI RESTORAN ===")

    id_pelanggan = input("ID Pelanggan: ").strip()

    pelanggan = cari_pelanggan(id_pelanggan)

    if pelanggan is None:
        print("Pelanggan tidak ditemukan!")
        return

    id_menu = input("ID Menu: ").strip()

    menu = cari_menu(id_menu)

    if menu is None:
        print("Menu tidak ditemukan!")
        return

    if menu.get_status() == "Habis":
        print("Menu sedang habis!")
        return

    try:
        jumlah = int(input("Jumlah pesanan: "))

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return

    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    id_transaksi = "TR" + str(len(daftar_transaksi) + 1)

    transaksi = Transaksi(
        id_transaksi, pelanggan, menu, jumlah
    )

    daftar_transaksi.append(transaksi)

    print("\nTransaksi berhasil dibuat!")
    transaksi.tampilkan_transaksi()


# Fungsi menampilkan data transaksi
def tampilkan_transaksi():
    print("\n=== DAFTAR TRANSAKSI ===")

    if not daftar_transaksi:
        print("Belum ada transaksi.")
        return

    for transaksi in daftar_transaksi:
        print("----------------------")
        transaksi.tampilkan_transaksi()


# Menu utama program
def main():
    while True:
        print("\n================================")
        print("       KASIR RESTORAN")
        print("================================")
        print("1. Tambah Data Menu")
        print("2. Tampilkan Data Menu")
        print("3. Cari Data Menu")
        print("4. Ubah Data Menu")
        print("5. Cek Status Menu")
        print("6. Tambah Data Pelanggan")
        print("7. Transaksi Penjualan")
        print("8. Tampilkan Transaksi")
        print("9. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_menu()

        elif pilihan == "2":
            tampilkan_menu()

        elif pilihan == "3":
            cari_data()

        elif pilihan == "4":
            ubah_data()

        elif pilihan == "5":
            cek_status()

        elif pilihan == "6":
            tambah_pelanggan()

        elif pilihan == "7":
            tambah_transaksi()

        elif pilihan == "8":
            tampilkan_transaksi()

        elif pilihan == "9":
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
