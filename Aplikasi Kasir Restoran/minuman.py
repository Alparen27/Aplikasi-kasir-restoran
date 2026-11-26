from menu import Menu


# Inheritance dari superclass Menu
class Minuman(Menu):

    def __init__(self, id_menu, nama, harga, ukuran, suhu):
        super().__init__(id_menu, nama, harga)

        # Attribute private
        self.__ukuran = ukuran
        self.__suhu = suhu

    # Getter dari attribute private
    def get_ukuran(self):
        return self.__ukuran

    def get_suhu(self):
        return self.__suhu

    # Method untuk mengubah ukuran minuman
    def ubah_ukuran(self, ukuran):
        self.__ukuran = ukuran

    # Method untuk mengubah suhu minuman
    def ubah_suhu(self, suhu):
        self.__suhu = suhu

    # Method menampilkan informasi minuman
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Ukuran  : {self.__ukuran}")
        print(f"Suhu    : {self.__suhu}")
