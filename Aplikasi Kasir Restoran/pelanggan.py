class Pelanggan:

    def __init__(self, id_pelanggan, nama, metode_pembayaran):
        # Atribut private
        self.__id_pelanggan = id_pelanggan
        self.__nama = nama
        self.__metode_pembayaran = metode_pembayaran

    # Getter dari atribut private
    def get_id(self):
        return self.__id_pelanggan

    def get_nama(self):
        return self.__nama

    def get_metode_pembayaran(self):
        return self.__metode_pembayaran

    # Method untuk menampilkan informasi pelanggan
    def tampilkan_info(self):
        print(f"ID Pelanggan       : {self.__id_pelanggan}")
        print(f"Nama Pelanggan     : {self.__nama}")
        print(f"Metode Pembayaran  : {self.__metode_pembayaran}")
