class Hewan:
    total_hewan = 0
    nama_klinik = "PawCare: Pet Clinic"
    jenis_terdaftar = ["Kucing", "Anjing", "Kelinci", "Capibara"]

    def __init__(self, nama, jenis, pemilik, umur, berat):
        self.nama = nama
        self.jenis = jenis
        self.pemilik = pemilik
        self.__umur = umur
        self.__berat = berat
        Hewan.total_hewan += 1

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai < 0:
            print(f"Umur ga valid: {nilai}")
            return
        self.__umur = nilai

    @property
    def berat(self):
        return self.__berat

    @berat.setter
    def berat(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai <= 0:
            print(f"Berat ga valid: {nilai}")
            return
        self.__berat = nilai

    def info(self):
        print(f"{self.nama} ({self.jenis}) milik {self.pemilik} - umur {self.__umur} tahun, berat {self.__berat} kg")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["jenis"], data["pemilik"], data["umur"], data["berat"])

    @staticmethod
    def validasi_jenis(jenis):
        return jenis in Hewan.jenis_terdaftar


class LayananHewan:
    total_layanan = 0
    biaya_admin = 5000
    kategori_tersedia = ["Perawatan", "Penitipan","Vaksinasi"]

    def __init__(self, nama_layanan, kategori, harga):
        self.nama_layanan = nama_layanan
        self.kategori = kategori
        self.__harga = harga
        LayananHewan.total_layanan += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai <= 0:
            print(f"Harga ga valid: {nilai}")
            return
        self.__harga = nilai

    def tampilkan(self):
        print(f"{self.nama_layanan} ({self.kategori}) - Rp{self.__harga:,}")

    @classmethod
    def ubah_biaya_admin(cls, biaya_baru):
        if biaya_baru < 0:
            print("Biaya admin gaboleh negatif")
            return
        cls.biaya_admin = biaya_baru

    @staticmethod
    def validasi_kategori(kategori):
        return kategori in LayananHewan.kategori_tersedia


class Transaksi:
    total_transaksi = 0
    status_tersedia = ["Menunggu.... (sabar.)", "Diproses boskyuh", "Selesai yeay!", "Dibatalkan"]
    nama_platform = "PawCare: Pet Clinic"

    def __init__(self, hewan, layanan, status="Menunggu.... (sabar.)"):
        Transaksi.total_transaksi += 1
        self.id_transaksi = Transaksi.total_transaksi
        self.hewan = hewan
        self.layanan = layanan
        self.status = status
        self.__total_bayar = layanan.harga + LayananHewan.biaya_admin

    @property
    def total_bayar(self):
        return self.__total_bayar

    @total_bayar.setter
    def total_bayar(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai < 0:
            print(f"Total bayar ga valid: {nilai}")
            return
        self.__total_bayar = nilai

    def ubah_status(self, status_baru):
        if not Transaksi.validasi_status(status_baru):
            print(f"Status '{status_baru}' tidak dikenal")
            return
        self.status = status_baru
        print(f"Transaksi #{self.id_transaksi} sekarang berstatus {self.status}")

    def struk(self):
        print(f"--- Struk Transaksi #{self.id_transaksi} ({Transaksi.nama_platform}) ---")
        print(f"Hewan   : {self.hewan.nama} ({self.hewan.jenis})")
        print(f"Layanan : {self.layanan.nama_layanan}")
        print(f"Status  : {self.status}")
        print(f"Total   : Rp{self.__total_bayar:,}")

    @classmethod
    def batalkan(cls, transaksi):
        transaksi.ubah_status("Dibatalkan")
        return transaksi

    @staticmethod
    def validasi_status(status):
        return status in Transaksi.status_tersedia


if __name__ == "__main__":
    kucing1 = Hewan("Milo", "Kucing", "Xie", 2, 4.5)
    data_anjing = {"nama": "fufufafa", "jenis": "Anjing", "pemilik": "Wowi", "umur": 3, "berat": 12}
    anjing1 = Hewan.dari_dict(data_anjing)

    perawatan = LayananHewan("Perawatan Kesehatan", "Perawatan", 100000)
    penitipan = LayananHewan("Penitipan 1 Malam", "Penitipan", 100000)

    trx1 = Transaksi(kucing1, perawatan)
    trx2 = Transaksi(anjing1, penitipan)

    print("=== Data Hewan ===")
    kucing1.info()
    anjing1.info()

    print("\n=== Data Layanan ===")
    perawatan.tampilkan()
    penitipan.tampilkan()

    print("\n=== Riwayat Transaksi ===")
    trx1.struk()
    trx2.struk()

    print("\n=== Uji Setter Hewan ===")
    kucing1.umur = 3
    print("Umur baru Milo:", kucing1.umur)
    kucing1.umur = -5
    kucing1.berat = 0

    print("\n=== Uji Setter Layanan ===")
    perawatan.harga = 80000
    print("Harga baru perawatan:", perawatan.harga)
    perawatan.harga = -1000

    print("\n=== Uji Ubah Status Transaksi ===")
    trx1.ubah_status("Selesai yeay!")
    trx1.ubah_status("Terbang")

    print("\n=== Uji Class Method ===")
    LayananHewan.ubah_biaya_admin(10000)
    trx3 = Transaksi(kucing1, penitipan)
    trx3.struk()
    Transaksi.batalkan(trx2)

    print("\n=== Uji Static Method ===")
    print(Hewan.validasi_jenis("Kucing"))
    print(Hewan.validasi_jenis("Naga"))
    print(LayananHewan.validasi_kategori("Perawatan"))
    print(Transaksi.validasi_status("Selesai yeay!"))

    print("\n=== Atribut Kelas ===")
    print("Total hewan terdaftar:", Hewan.total_hewan)
    print("Total layanan terdaftar:", LayananHewan.total_layanan)
    print("Total transaksi:", Transaksi.total_transaksi)
    print("Nama klinik:", Hewan.nama_klinik)