class Menu:

    def __init__(self, id_menu, nama, harga):
        # Attribute private untuk enkapsulasi
        self.__id_menu = id_menu
        self.__nama = nama
        self.__harga = harga
        self.__status = "Tersedia"

    # Getter untuk mengambil nilai attribute private
    def get_id_menu(self):
        return self.__id_menu

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_status(self):
        return self.__status

    # Method untuk mengubah harga
    def ubah_harga(self, harga_baru):
        self.__harga = harga_baru

    # Method untuk mengubah status menu
    def ubah_status(self, status):
        self.__status = status

    # Method untuk menampilkan informasi menu
    def tampilkan_info(self):
        print(f"ID      : {self.__id_menu}")
        print(f"Nama    : {self.__nama}")
        print(f"Harga   : Rp{self.__harga}")
        print(f"Status  : {self.__status}")
