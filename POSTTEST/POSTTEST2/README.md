# PawCare - Sistem Layanan Perawatan Hewan Peliharaan

Program OOP buat catat data hewan peliharaan, layanan yang ditawarin klinik, sama transaksi pemesanannya. Dibangun bertahap ngikutin materi yang udah dipelajari: Class & Object, Atribut & Method, Encapsulation, sampe Inheritance dan Relasi UML.

## Struktur Class

### Hewan (superclass) -> Kucing, Anjing (subclass)

**Hewan** isinya data dasar yang bakal diwarisin ke semua jenis hewan.
- Atribut kelas: `total_hewan`, `nama_klinik`, `jenis_terdaftar`
- Atribut instance (public): `nama`, `jenis`, `pemilik`
- Atribut instance (private): `__umur`, `__berat` — cuma bisa diubah lewat property, gak bisa diakses langsung bahkan sama subclass-nya sendiri (kena name mangling)
- Atribut instance (protected): `_kondisi` — status kesehatan, sengaja protected karena subclass boleh ubah langsung tanpa lewat getter-setter
- Method `info()` buat nampilin data hewan
- Staticmethod `validasi_jenis()` buat ngecek jenis hewannya kedaftar apa nggak

**Kucing(Hewan)** manggil `super().__init__()`, nambahin atribut unik `sudah_steril`, override `info()` buat nambahin baris status steril, dan punya `update_kesehatan()` yang langsung ubah `_kondisi`. Punya `dari_dict()` sendiri buat bikin objek dari dictionary.

**Anjing(Hewan)** sama kayak Kucing, tapi atribut uniknya `ras`, dan `info()`-nya di-override beda: ngecek `berat` buat nentuin "anjing gede" apa "anjing kecil".

### LayananHewan (superclass) -> Perawatan, Penitipan (subclass)

**LayananHewan** data dasar layanan yang ditawarin.
- Atribut kelas: `total_layanan`, `biaya_admin`, `kategori_tersedia`
- Atribut instance (public): `nama_layanan`, `kategori`
- Atribut instance (private): `__harga` — sama kayak umur/berat, cuma lewat property
- Method `tampilkan()` buat nampilin detail layanan
- Classmethod `ubah_biaya_admin()` buat ganti biaya admin yang berlaku ke semua transaksi
- Staticmethod `validasi_kategori()` buat ngecek kategorinya valid apa nggak

**Perawatan(LayananHewan)** manggil `super().__init__()`, atribut uniknya `jenis_perawatan`, override `tampilkan()` nambahin baris jenis perawatannya.

**Penitipan(LayananHewan)** sama, atribut uniknya `durasi_hari`, `tampilkan()` juga di-override nambahin baris durasi penitipan.

### Transaksi & Nota

**Transaksi** nyambungin objek `Hewan` sama `LayananHewan` jadi satu pemesanan.
- Atribut kelas: `total_transaksi`, `status_tersedia` (sengaja agak absurd: "Menunggu.... (sabar.)", "Diproses boskyuh", "Selesai yeay!", "Dibatalkan"), `nama_platform`
- Atribut instance (private): `__total_bayar`, dihitung otomatis dari harga layanan + biaya admin
- Method `ubah_status()` (udah divalidasi dulu) dan `struk()` buat nampilin ringkasan
- Classmethod `batalkan()`, staticmethod `validasi_status()`

**Nota** cuma nyimpen id transaksi, nama layanan, sama totalnya. Dibikin langsung di dalem `Transaksi.__init__()`, jadi nempel total ke transaksi itu doang.

### Resepsionis
Class kecil yang nerima `Hewan` sama `LayananHewan` sebagai parameter method `buat_transaksi()`, dipake sebentar buat bikin `Transaksi`, abis itu gak disimpen lagi.

## Inheritance

- 2 pasang superclass-subclass: `Hewan` -> `Kucing`/`Anjing`, dan `LayananHewan` -> `Perawatan`/`Penitipan`
- Semua subclass manggil `super().__init__(...)` buat ngewarisin data dari induknya
- Tiap subclass punya atribut unik sendiri yang gak ada di induk maupun subclass lain
- Method overriding: `info()` di Kucing & Anjing, `tampilkan()` di Perawatan & Penitipan, masing-masing beda logikanya
- Protected (`_kondisi`) dipake buat data yang emang perlu diutak-atik langsung sama subclass
- Private (`__umur`, `__berat`, `__harga`) dipake buat data yang bener-bener gak boleh diutak-atik langsung, baik dari luar maupun dari subclass-nya sendiri

## Relasi UML

### Asosiasi — Resepsionis
`Resepsionis.buat_transaksi(hewan, layanan)` nerima objek `Hewan` dan `LayananHewan` cuma sebagai parameter doang, dipake sesaat buat bikin `Transaksi`, terus gak disimpen jadi atribut permanen di `Resepsionis`.

### Agregasi — Transaksi ke Hewan & LayananHewan
`Transaksi` nyimpen objek `hewan` dan `layanan` yang dibuat di luar (sebelum transaksinya ada) lewat konstruktor. Kalau transaksinya dihapus, hewan dan layanannya tetep ada, gak ikut ilang. Dibuktiin di kode testing: abis `del trx1`, `kucing1.info()` dan `perawatan.tampilkan()` masih bisa dipanggil normal.

### Komposisi — Transaksi dan Nota
`Transaksi` bikin objek `Nota` sendiri di dalem `__init__()`-nya (bukan dikirim dari luar). Nota ini nempel total ke transaksi tersebut dan gak punya arti sendiri di luar konteks transaksi itu.

## Cara Jalanin

```bash
python PawCarePart2.py
```
(terserah, sesuai kan aja sama nama file nya apa. karena ini aku bedain jadi namanya ku update PawcarePart2 kemarin udah part 1 nya. intinya setiap nama filenya baru, langsung ganti aja)

## Panduan Ngetes

Urutan yang keliatan pas program dijalanin:

1. **Bikin objek** - `Kucing` lewat constructor biasa, `Anjing` lewat `dari_dict()`, `Perawatan` dan `Penitipan` lewat constructor masing-masing.
2. **Method overriding** - `info()` buat kucing/anjing dan `tampilkan()` buat perawatan/penitipan, hasilnya beda-beda sesuai subclass-nya.
3. **Cek relasi pewarisan** - `isinstance()` sama `issubclass()` buat buktiin subclass-subclass itu beneran turunan superclass-nya.
4. **Protected** - `update_kesehatan()` dipanggil dari objek Kucing, langsung ngubah `_kondisi` tanpa lewat getter-setter.
5. **Asosiasi** - `Resepsionis` bikin transaksi dari hewan dan layanan yang udah ada.
6. **Komposisi** - `struk()` nampilin `Nota` yang nempel ke transaksinya masing-masing.
7. **Agregasi** - salah satu transaksi dihapus (`del trx1`), terus dibuktiin hewan dan layanannya masih bisa dipanggil, artinya gak ikut kehapus.
8. **Setter valid & gak valid** - umur/berat/harga dicoba diisi nilai bener sama nilai ngasal, yang ngasal ditolak.
9. **Classmethod & staticmethod** - `ubah_biaya_admin()`, `batalkan()`, `validasi_jenis()`, `validasi_kategori()`, `validasi_status()` semua dites.
10. **Atribut kelas** - di akhir, `total_hewan`, `total_layanan`, `total_transaksi` kecetak buat nunjukin nilainya kebarui otomatis tiap ada objek baru.