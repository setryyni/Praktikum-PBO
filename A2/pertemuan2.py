# class Nasabah:

#     def __init__(self,nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

# nama = input ("masukan nama:")
# saldo = input("masukan saldo:")

# user = Nasabah(nama, saldo)
# dapa = Nasabah("dapa", 5000)
# # print(user.nama)
# # print(user.saldo)
# print(dapa.nama)
# print(dapa.saldo)

# class Karyawan:
#     def __init__(self, nama, gaji):
#         self.nama = nama
#         self._gaji = gaji # protected, hanya "disarankan" diakses dari dalam

# class Manager(Karyawan):
#     def tampilkan_gaji(self):
#         # subclass tetap bisa mengakses atribut protected milik parent
#         print(f"Gaji {self.nama}: {self._gaji}")

# manager = Manager("Daffa", 12000000)
# manager.tampilkan_gaji()
# print(manager._gaji) # masih bisa diakses, tapi secara konvensi sebaiknya

class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo # private
    def tarik_saldo(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup.")
        elif jumlah <= 0:
            print("Jumlah penarikan tidak valid.")
        else:
            self.__saldo -= jumlah
            print(f"Berhasil menarik {jumlah}. Sisa saldo: {self.__saldo}")
    def cek_saldo(self):
        print(f"Saldo saat ini: {self.__saldo}")

rekening = RekeningBank("Budi", 100000)
rekening.tarik_saldo(30000)
rekening.cek_saldo()
# print(rekening.__saldo) # AttributeError, karena sudah di-name-mangling

print(rekening._RekeningBank__saldo) # masih bisa diakses, tapi secara konvensi sebaiknya tidak