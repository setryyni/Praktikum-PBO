class Nasabah:
    def __init__(self, nama, nomor_rekening):
        self.nama = nama
        self.nomor_rekening = nomor_rekening

    def tarik_tunai(self, atm, jumlah):
        atm.saldo_kas -= jumlah

class MesinAtm:
    def __init__(self, id_atm, lokasi, saldo_kas):
        self.id_atm = id_atm
        self.lokasi = lokasi
        self.saldo_kas = saldo_kas

dapa = Nasabah("Dapa", 123456789)
atm_pusat = MesinAtm("pusat", "samrinda", 5000000)

dapa.tarik_tunai(atm_pusat, 500)

print(atm_pusat.saldo_kas)  