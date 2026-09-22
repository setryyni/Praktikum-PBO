# PawCare - Sistem Layanan Perawatan Hewan Peliharaan

Program ini dibuat buat latihan OOP di Python, ceritanya sistem sederhana buat catat data hewan peliharaan, layanan yang ditawarin, sama transaksi pemesanan layanannya.

## Struktur Class

Ada 3 class utama, semuanya berdiri sendiri, tapi saling nyambung lewat objek satu sama lain.

### 1. Hewan
Nyimpen data hewan yang terdaftar di klinik.

- Atribut kelas: `total_hewan`, `nama_klinik`, `jenis_terdaftar`
- Atribut instance (public): `nama`, `jenis`, `pemilik`
- Atribut instance (private): `__umur`, `__berat`
- Property `umur` dan `berat` punya setter yang nolak kalau nilainya negatif (berat juga gak boleh 0)
- Method `info()` buat nampilin data hewannya
- Classmethod `dari_dict()` buat bikin objek `Hewan` langsung dari dictionary
- Staticmethod `validasi_jenis()` buat ngecek jenis hewannya kedaftar apa nggak

### 2. LayananHewan
Nyimpen data layanan yang tersedia, ada Perawatan, Penitipan, sama Vaksinasi.

- Atribut kelas: `total_layanan`, `biaya_admin`, `kategori_tersedia`
- Atribut instance (public): `nama_layanan`, `kategori`
- Atribut instance (private): `__harga`
- Property `harga` setternya nolak kalau harganya 0 atau minus
- Method `tampilkan()` buat nampilin detail layanan
- Classmethod `ubah_biaya_admin()` buat ganti biaya admin yang berlaku ke semua transaksi
- Staticmethod `validasi_kategori()` buat ngecek kategorinya valid apa nggak

### 3. Transaksi
Nyambungin objek `Hewan` sama `LayananHewan` jadi satu pemesanan.

- Atribut kelas: `total_transaksi`, `status_tersedia`, `nama_platform`
- Atribut instance (public): `id_transaksi`, `hewan`, `layanan`, `status`
- Atribut instance (private): `__total_bayar`, dihitung otomatis dari harga layanan + biaya admin
- Property `total_bayar` setternya nolak kalau nilainya minus
- Method `ubah_status()` buat ganti status transaksi (udah divalidasi dulu), sama `struk()` buat nampilin ringkasan transaksinya
- Classmethod `batalkan()` buat batalin satu transaksi
- Staticmethod `validasi_status()` buat ngecek statusnya valid apa nggak

Oiya, status transaksinya sengaja dibikin agak absurd biar gak monoton: `"Menunggu.... (sabar.)"`, `"Diproses boskyuh"`, `"Selesai yeay!"`, sama `"Dibatalkan"`. Jadi kalau manggil `ubah_status()`, tulisan statusnya harus persis sama kayak yang ada di list itu.

## Cara Jalanin

```bash
python PawCarePart1.py
```

Semua contoh pemakaiannya udah ditulis di bagian `if __name__ == "__main__":`, jadi tinggal run aja gak perlu input manual apa-apa.

## Panduan Ngetes

Pas dijalanin, programnya bakal nampilin berurutan:

1. **Data awal** - dua objek `Hewan` (satu dibikin lewat constructor biasa, satu lagi lewat `dari_dict()`), dua objek `LayananHewan`, dan dua objek `Transaksi`.
2. **Setter yang valid** - umur kucing diganti jadi 3 sama harga perawatan diganti jadi 80000, keduanya berhasil kesimpen.
3. **Setter yang gak valid** - dicoba ganti umur jadi -5, berat jadi 0, sama harga jadi -1000. Semuanya ditolak dan programnya nge-print pesan error, nilainya tetep yang lama.
4. **Ubah status transaksi** - dites pakai status yang bener (`"Selesai yeay!"`) sama status ngasal (`"Terbang"`) buat liat bedanya.
5. **Classmethod** - `ubah_biaya_admin()` buat ganti biaya admin ke semua transaksi baru, sama `batalkan()` buat batalin transaksi yang udah ada.
6. **Staticmethod** - `validasi_jenis()`, `validasi_kategori()`, sama `validasi_status()` dipanggil langsung dari classnya, gak perlu bikin objek dulu.
7. **Atribut kelas** - di bagian akhir keliatan `total_hewan`, `total_layanan`, sama `total_transaksi` naik otomatis tiap kali ada objek baru.
