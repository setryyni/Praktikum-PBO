from abc import ABC, abstractmethod

class Pemilik:
    def __init__(self, nama, kontak):
        self.nama = nama
        self.kontak = kontak
        self._daftar_hewan = []

    def tambah_hewan(self, hewan):
        if hewan not in self._daftar_hewan:
            self._daftar_hewan.append(hewan)
            hewan.pemilik = self

    def keluarkan_hewan(self, hewan):
        if hewan in self._daftar_hewan:
            self._daftar_hewan.remove(hewan)
            hewan.pemilik = None

    def __len__(self):
        return len(self._daftar_hewan)

    def __str__(self):
        return f"{self.nama} ({len(self)} hewan)"


class Hewan(ABC):
    total_hewan = 0
    nama_klinik = "PawCare: Pet Clinic"

    def __init__(self, nama, jenis, umur, berat):
        self.nama = nama
        self.jenis = jenis
        self.pemilik = None
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


    @abstractmethod
    def suara(self):
        pass

    @abstractmethod
    def info_perawatan(self):
        pass


    def update_kesehatan(self, catatan):
        self._kondisi = catatan

    def info(self):
        print(f"{self} | kondisi: {self._kondisi}")

    def __str__(self):
        nama_pemilik = self.pemilik.nama if self.pemilik else "-"
        return (f"{self.nama} ({self.jenis}) - {self.__umur} tahun, "
                f"{self.__berat} kg, pemilik: {nama_pemilik}")


class Kucing(Hewan):
    def __init__(self, nama, umur, berat, sudah_steril):
        super().__init__(nama, "Kucing", umur, berat)
        self.sudah_steril = sudah_steril

    def suara(self):
        return "Meong~"

    def info_perawatan(self):
        steril = "udah steril" if self.sudah_steril else "belum steril, jadwalin konsultasi"
        return f"Sikat bulu 2x seminggu, potong kuku tiap bulan ({steril})"


class Anjing(Hewan):
    def __init__(self, nama, umur, berat, ras):
        super().__init__(nama, "Anjing", umur, berat)
        self.ras = ras

    def suara(self):
        return "Guk guk!"

    def info_perawatan(self):
        menit = 60 if self.berat > 20 else 30
        return f"Jalan pagi {menit} menit tiap hari, mandi 2 minggu sekali (ras {self.ras})"


class Kelinci(Hewan):
    def __init__(self, nama, umur, berat, jenis_bulu):
        super().__init__(nama, "Kelinci", umur, berat)
        self.jenis_bulu = jenis_bulu

    def suara(self):
        return "*mengendus pelan*"

    def info_perawatan(self):
        return f"Hay segar tiap hari, bulu {self.jenis_bulu} disisir seminggu sekali"


class LayananHewan(ABC):
    total_layanan = 0
    biaya_admin = 5000

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

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def proses_layanan(self, hewan):
        pass


    def jalankan(self, hewan):
        print(f"[{self.kategori}] {self.nama_layanan} untuk {hewan.nama}")
        self.proses_layanan(hewan)
        print(f"  Biaya layanan: Rp{self.hitung_biaya():,}")

    @classmethod
    def ubah_biaya_admin(cls, biaya_baru):
        if biaya_baru < 0:
            print("Biaya admin gaboleh negatif")
            return
        cls.biaya_admin = biaya_baru


    def __lt__(self, other):
        return self.hitung_biaya() < other.hitung_biaya()

    def __add__(self, other):
        return self.hitung_biaya() + other.hitung_biaya()

    def __str__(self):
        return f"{self.nama_layanan} ({self.kategori}) - Rp{self.hitung_biaya():,}"


class Perawatan(LayananHewan):
    def __init__(self, nama_layanan, harga, jenis_perawatan):
        super().__init__(nama_layanan, "Perawatan", harga)
        self.jenis_perawatan = jenis_perawatan

    def hitung_biaya(self):
        return self.harga

    def proses_layanan(self, hewan):
        hewan.update_kesehatan(f"Selesai {self.jenis_perawatan}")
        print(f"  {hewan.nama} dicek lewat {self.jenis_perawatan}")


class Penitipan(LayananHewan):
    def __init__(self, nama_layanan, harga_per_hari, durasi_hari):
        super().__init__(nama_layanan, "Penitipan", harga_per_hari)
        self.durasi_hari = durasi_hari

    def hitung_biaya(self):
        return self.harga * self.durasi_hari

    def proses_layanan(self, hewan):
        print(f"  {hewan.nama} dititipkan selama {self.durasi_hari} hari")


class Vaksinasi(LayananHewan):
    def __init__(self, nama_layanan, harga, nama_vaksin):
        super().__init__(nama_layanan, "Vaksinasi", harga)
        self.nama_vaksin = nama_vaksin

    def hitung_biaya(self):
        return self.harga

    def proses_layanan(self, hewan):
        hewan.update_kesehatan(f"Divaksin {self.nama_vaksin}")
        print(f"  {hewan.nama} disuntik vaksin {self.nama_vaksin}")


class Nota:
    def __init__(self, id_transaksi, item, total):
        self.id_transaksi = id_transaksi
        self.item = item
        self.total = total

    def __str__(self):
        return f"[Nota #{self.id_transaksi}] {self.item} - Rp{self.total:,}"


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
        self.__total_bayar = layanan.hitung_biaya() + LayananHewan.biaya_admin

        self._nota = Nota(self.id_transaksi, layanan.nama_layanan, self.__total_bayar)

    @property
    def total_bayar(self):
        return self.__total_bayar

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


class NotifWhatsApp:
    def __init__(self, nomor):
        self.nomor = nomor

    def kirim(self, pesan):
        print(f"  [WA -> {self.nomor}] {pesan}")


class NotifSMS:
    def __init__(self, nomor):
        self.nomor = nomor

    def kirim(self, pesan):
        print(f"  [SMS -> {self.nomor}] {pesan}")


class NotifEmail:
    def __init__(self, alamat):
        self.alamat = alamat

    def kirim(self, pesan):
        print(f"  [EMAIL -> {self.alamat}] {pesan}")


def beritahu_pemilik(kanal_list, pesan):
    for kanal in kanal_list:
        kanal.kirim(pesan)


class Resepsionis:
    def __init__(self, nama, kanal_notif):
        self.nama = nama
        self._kanal = kanal_notif

    def buat_transaksi(self, hewan, layanan):
        print(f"{self.nama} lagi proses pemesanan buat {hewan.nama}...")
        trx = Transaksi(hewan, layanan)
        beritahu_pemilik(self._kanal,
                         f"Pesanan #{trx.id_transaksi} ({layanan.nama_layanan}) "
                         f"untuk {hewan.nama} dicatat. Total Rp{trx.total_bayar:,}")
        return trx


class Klinik:
    def __init__(self, nama):
        self.nama = nama
        self._hewan = []
        self._layanan = []
        self._transaksi = []


    def tambah_hewan(self, hewan, pemilik):
        pemilik.tambah_hewan(hewan)
        self._hewan.append(hewan)

    def tambah_layanan(self, layanan):
        self._layanan.append(layanan)

    def tambah_transaksi(self, transaksi):
        self._transaksi.append(transaksi)


    def tampilkan_hewan(self):
        for h in self._hewan:
            h.info()

    def tampilkan_layanan(self):
        for l in self._layanan:
            print(l)

    def tampilkan_riwayat(self):
        for t in self._transaksi:
            t.struk()

    @property
    def daftar_hewan(self):
        return list(self._hewan)

    @property
    def daftar_layanan(self):
        return list(self._layanan)


    def ubah_data_hewan(self, hewan, umur=None, berat=None):
        if umur is not None:
            hewan.umur = umur
        if berat is not None:
            hewan.berat = berat

    def ubah_kontak_pemilik(self, pemilik, kontak_baru):
        pemilik.kontak = kontak_baru

    def ubah_status(self, transaksi, status_baru):
        transaksi.ubah_status(status_baru)


    def hapus_hewan(self, hewan):
        if hewan in self._hewan:
            self._hewan.remove(hewan)
            if hewan.pemilik:
                hewan.pemilik.keluarkan_hewan(hewan)

    def batalkan_transaksi(self, transaksi):
        Transaksi.batalkan(transaksi)


def judul(teks):
    print(f"\n=== {teks} ===")


if __name__ == "__main__":
    judul("Bukti Abstraksi: Abstract Class Gak Bisa Diinstansiasi")
    try:
        Hewan("Test", "Apa aja", 1, 1)
    except TypeError as e:
        print(f"TypeError: {e}")
    try:
        LayananHewan("Test", "Apa aja", 1000)
    except TypeError as e:
        print(f"TypeError: {e}")

    judul("Create: Pemilik, Hewan, Layanan")
    xie = Pemilik("Xie", "0812-1111-2222")
    wowi = Pemilik("Wowi", "0813-3333-4444")

    milo = Kucing("Milo", 2, 4.5, True)
    fufufafa = Anjing("fufufafa", 3, 22, "Golden Retriever")
    bunny = Kelinci("Bunny", 1, 1.8, "lebat")

    perawatan = Perawatan("Perawatan Kesehatan", 100000, "Checkup Rutin")
    penitipan = Penitipan("Penitipan per Malam", 80000, 3)
    vaksin = Vaksinasi("Vaksin Tahunan", 150000, "Rabies")

    klinik = Klinik(Hewan.nama_klinik)
    klinik.tambah_hewan(milo, xie)
    klinik.tambah_hewan(fufufafa, wowi)
    klinik.tambah_hewan(bunny, xie)
    for l in (perawatan, penitipan, vaksin):
        klinik.tambah_layanan(l)

    judul("Read: Daftar Hewan & Layanan")
    klinik.tampilkan_hewan()
    print()
    klinik.tampilkan_layanan()

    judul("Polimorfisme via Pewarisan: info_perawatan() & suara()")
    for h in klinik.daftar_hewan:
        print(f"{h.nama:<9}: {h.suara()}")
        print(f"           {h.info_perawatan()}")

    judul("Polimorfisme via Pewarisan: jalankan() -> proses_layanan()")
    for l in klinik.daftar_layanan:
        l.jalankan(milo)

    judul("Duck Typing: Notifikasi Multi-Kanal")
    kanal = [NotifWhatsApp("0812-1111-2222"), NotifSMS("0812-1111-2222"),
             NotifEmail("xie@mail.com")]
    beritahu_pemilik(kanal, "Milo sudah selesai dirawat, silakan dijemput.")

    judul("Operator Overloading")
    print("print(vaksin)          :", vaksin)
    print("perawatan + penitipan  : Rp{:,}".format(perawatan + penitipan))
    print("perawatan < penitipan  :", perawatan < penitipan)
    print("len(xie)               :", len(xie))
    print("Layanan termurah -> termahal:")
    for l in sorted(klinik.daftar_layanan):
        print("  ", l)

    judul("Asosiasi: Resepsionis Bikin Transaksi (DIP: kanal disuntikkan)")
    nindy = Resepsionis("Nindy", [NotifWhatsApp("0812-1111-2222"), NotifEmail("xie@mail.com")])
    trx1 = nindy.buat_transaksi(milo, perawatan)
    trx2 = nindy.buat_transaksi(fufufafa, penitipan)
    trx3 = nindy.buat_transaksi(bunny, vaksin)
    for t in (trx1, trx2, trx3):
        klinik.tambah_transaksi(t)

    judul("Komposisi: Struk & Nota Nempel ke Transaksi")
    klinik.tampilkan_riwayat()

    judul("Agregasi: Hewan & Layanan Tetap Ada Walau Transaksi Dihapus")
    del trx3
    bunny.info()
    vaksin.jalankan(bunny)

    judul("Update: Data Hewan, Kontak Pemilik, Status Transaksi")
    klinik.ubah_data_hewan(milo, umur=3, berat=4.8)
    klinik.ubah_data_hewan(milo, umur=-5, berat=0)
    klinik.ubah_kontak_pemilik(xie, "0899-9999-0000")
    print("Kontak baru Xie:", xie.kontak)
    klinik.ubah_status(trx1, "Selesai yeay!")
    klinik.ubah_status(trx1, "Terbang")
    milo.info()

    judul("Delete: Hapus Hewan & Batalkan Transaksi")
    klinik.hapus_hewan(bunny)
    print("Hewan di klinik:", [h.nama for h in klinik.daftar_hewan])
    print("Pemilik Xie    :", xie)
    print("Objek bunny masih ada di memori:", bunny.nama)
    klinik.batalkan_transaksi(trx2)

    judul("Class Method: Ubah Biaya Admin")
    LayananHewan.ubah_biaya_admin(10000)
    trx4 = nindy.buat_transaksi(milo, penitipan)
    trx4.struk()

    judul("Atribut Kelas")
    print("Total hewan terdaftar  :", Hewan.total_hewan)
    print("Total layanan terdaftar:", LayananHewan.total_layanan)
    print("Total transaksi        :", Transaksi.total_transaksi)
    print("Nama klinik            :", Hewan.nama_klinik)