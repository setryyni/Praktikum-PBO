# class Animal:
#     def __init__(self, nama, umur, warna_bulu, berbisa):
#         self.nama = nama
#         self.umur = umur
#         self.warna_bulu = warna_bulu
#         self.berbisa = berbisa

#     def makan(self):
#         print(f"{self.nama} sedang makan")

# kucing = Animal("oren", 2, "oren", None)
# ular = Animal("cobra", 1, None, True)

class Animal:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Mamalia(Animal):
    def __init__(self, nama, umur, warna_bulu):
        super().__init__(nama, umur)
        # self.nama = nama
        # self.umur = umur
        self.warna_bulu = warna_bulu

    def makan(self):
        print(f"{self.nama} sedang makan")

class Reptile(Animal):
    def __init__(self, nama, umur, berbisa):
        # self.nama = nama
        # self.umur = umur
        self.berbisa = berbisa

kucing = Mamalia("oren", 2, "oren")
print(kucing.nama)
kucing.makan()