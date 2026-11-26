class Transaksi:

    # Relasi association dengan objek Pelanggan dan Menu
    def __init__(self, id_transaksi, pelanggan, menu, jumlah):
        self.__id_transaksi = id_transaksi
        self.__pelanggan = pelanggan
        self.__menu = menu
        self.__jumlah = jumlah

        # Mengambil metode pembayaran dari objek pelanggan
        self.__metode_pembayaran = pelanggan.get_metode_pembayaran()

        # Menghitung total pembayaran
        self.__total = menu.get_harga() * jumlah

    # Getter
    def get_id_transaksi(self):
        return self.__id_transaksi

    def get_total(self):
        return self.__total

    def get_status(self):
        return self.__menu.get_status()

    def get_metode_pembayaran(self):
        return self.__metode_pembayaran

    # Method menghitung total pembayaran
    def hitung_total(self):
        self.__total = self.__menu.get_harga() * self.__jumlah
        return self.__total

    # Method menampilkan transaksi
    def tampilkan_transaksi(self):
        print("\n===== DETAIL TRANSAKSI =====")
        print(f"ID Transaksi      : {self.__id_transaksi}")
        print(f"Pelanggan         : {self.__pelanggan.get_nama()}")
        print(f"Menu              : {self.__menu.get_nama()}")
        print(f"Jumlah            : {self.__jumlah}")
        print(f"Metode Pembayaran : {self.__metode_pembayaran}")
        print(f"Total Pembayaran  : Rp{self.hitung_total():,}")
        print(f"Status            : {self.get_status()}")
