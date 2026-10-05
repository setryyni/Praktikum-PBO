class Nota:
    def __init__(self, id_transaksi, item, total):
        self.id_transaksi = id_transaksi
        self.item = item
        self.total = total

    def __str__(self):
        return f"[Nota #{self.id_transaksi}] {self.item} - Rp{self.total:,}"


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
        self._kondisi = "Sehat"
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
        print(f"{self.nama} ({self.jenis}) milik {self.pemilik} - umur {self.__umur} tahun, berat {self.__berat} kg, kondisi: {self._kondisi}")

    @staticmethod
    def validasi_jenis(jenis):
        return jenis in Hewan.jenis_terdaftar


class Kucing(Hewan):
    def __init__(self, nama, pemilik, umur, berat, sudah_steril):
        super().__init__(nama, "Kucing", pemilik, umur, berat)
        self.sudah_steril = sudah_steril

    def info(self):
        super().info()
        status = "udah steril" if self.sudah_steril else "belum steril"
        print(f"  Status: {status}")

    def update_kesehatan(self, catatan):
        self._kondisi = catatan
        print(f"Kondisi kesehatan {self.nama} diupdate jadi: {self._kondisi}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["pemilik"], data["umur"], data["berat"], data["sudah_steril"])


class Anjing(Hewan):
    def __init__(self, nama, pemilik, umur, berat, ras):
        super().__init__(nama, "Anjing", pemilik, umur, berat)
        self.ras = ras

    def info(self):
        super().info()
        ukuran = "anjing gede" if self.berat > 20 else "anjing kecil"
        print(f"  Ras: {self.ras} ({ukuran})")

    def update_kesehatan(self, catatan):
        self._kondisi = catatan
        print(f"Kondisi kesehatan {self.nama} diupdate jadi: {self._kondisi}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["pemilik"], data["umur"], data["berat"], data["ras"])


class LayananHewan:
    total_layanan = 0
    biaya_admin = 5000
    kategori_tersedia = ["Perawatan", "Penitipan", "Vaksinasi"]

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
        print(f"{self.nama_layanan} ({self.kategori}) - Rp{self.harga:,}")

    @classmethod
    def ubah_biaya_admin(cls, biaya_baru):
        if biaya_baru < 0:
            print("Biaya admin gaboleh negatif")
            return
        cls.biaya_admin = biaya_baru

    @staticmethod
    def validasi_kategori(kategori):
        return kategori in LayananHewan.kategori_tersedia


class Perawatan(LayananHewan):
    def __init__(self, nama_layanan, harga, jenis_perawatan):
        super().__init__(nama_layanan, "Perawatan", harga)
        self.jenis_perawatan = jenis_perawatan

    def tampilkan(self):
        super().tampilkan()
        print(f"  Jenis perawatan: {self.jenis_perawatan}")


class Penitipan(LayananHewan):
    def __init__(self, nama_layanan, harga, durasi_hari):
        super().__init__(nama_layanan, "Penitipan", harga)
        self.durasi_hari = durasi_hari

    def tampilkan(self):
        super().tampilkan()
        print(f"  Durasi penitipan: {self.durasi_hari} hari")


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
        self._nota = Nota(self.id_transaksi, layanan.nama_layanan, self.__total_bayar)

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
        print(f"Layanan : {self.layanan.nama_layanan} ({self.layanan.kategori})")
        print(f"Status  : {self.status}")
        print(self._nota)

    @classmethod
    def batalkan(cls, transaksi):
        transaksi.ubah_status("Dibatalkan")
        return transaksi

    @staticmethod
    def validasi_status(status):
        return status in Transaksi.status_tersedia


class Resepsionis:
    def __init__(self, nama):
        self.nama = nama

    def buat_transaksi(self, hewan, layanan):
        print(f"{self.nama} lagi proses pemesanan buat {hewan.nama}...")
        return Transaksi(hewan, layanan)


if __name__ == "__main__":
    kucing1 = Kucing("Milo", "Xie", 2, 4.5, True)
    data_anjing = {"nama": "fufufafa", "pemilik": "Wowi", "umur": 3, "berat": 22, "ras": "Golden Retriever"}
    anjing1 = Anjing.dari_dict(data_anjing)

    perawatan = Perawatan("Perawatan Kesehatan", 100000, "Checkup Rutin")
    penitipan = Penitipan("Penitipan 1 Malam", 100000, 1)

    resepsionis = Resepsionis("Nindy")

    print("=== Info Hewan (Method Overriding) ===")
    kucing1.info()
    anjing1.info()

    print("\n=== Info Layanan (Method Overriding) ===")
    perawatan.tampilkan()
    penitipan.tampilkan()

    print("\n=== Cek Relasi Pewarisan ===")
    print(isinstance(kucing1, Hewan))
    print(isinstance(anjing1, Kucing))
    print(issubclass(Anjing, Hewan))
    print(isinstance(perawatan, LayananHewan))
    print(issubclass(Penitipan, LayananHewan))

    print("\n=== Protected: Subclass Ubah Kondisi Kesehatan Langsung ===")
    kucing1.update_kesehatan("Flu ringan")
    kucing1.info()

    print("\n=== Asosiasi: Resepsionis Bikin Transaksi ===")
    trx1 = resepsionis.buat_transaksi(kucing1, perawatan)
    trx2 = resepsionis.buat_transaksi(anjing1, penitipan)

    print("\n=== Riwayat Transaksi (Komposisi: Nota) ===")
    trx1.struk()
    trx2.struk()

    print("\n=== Agregasi: Hewan & Layanan Tetap Ada Walau Transaksinya Dihapus ===")
    del trx1
    kucing1.info()
    perawatan.tampilkan()

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
    trx2.ubah_status("Selesai yeay!")
    trx2.ubah_status("Terbang")

    print("\n=== Uji Class Method ===")
    LayananHewan.ubah_biaya_admin(10000)
    trx3 = resepsionis.buat_transaksi(kucing1, penitipan)
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