from menu import Menu


# Inheritance dari superclass Menu
class Makanan(Menu):

    def __init__(self, id_menu, nama, harga, jenis, level_pedas):
        super().__init__(id_menu, nama, harga)

        # Atribut private
        self.__jenis = jenis
        self.__level_pedas = level_pedas

    # Getter atribut private
    def get_jenis(self):
        return self.__jenis

    def get_level_pedas(self):
        return self.__level_pedas

    # Method untuk mengubah level pedas
    def ubah_level_pedas(self, level):
        self.__level_pedas = level

    # Method menampilkan informasi makanan
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis   : {self.__jenis}")
        print(f"Pedas   : {self.__level_pedas}")
