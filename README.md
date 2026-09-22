# PawCare - Sistem Layanan Perawatan Hewan Peliharaan

Program ini merupakan implementasi konsep Pemrograman Berorientasi Objek (PBO) berupa sistem sederhana untuk mengelola data hewan peliharaan, layanan yang ditawarkan, serta transaksi pemesanan layanan.

## Struktur Class

Program terdiri atas tiga class utama yang saling berinteraksi melalui objek, tanpa menggunakan pewarisan (inheritance).

### 1. Hewan
Menyimpan data hewan peliharaan yang terdaftar.

- Atribut kelas: `total_hewan`, `nama_klinik`, `jenis_terdaftar`
- Atribut instance (public): `nama`, `jenis`, `pemilik`
- Atribut instance (private): `__umur`, `__berat`
- Property: `umur` dan `berat`, masing-masing dengan getter dan setter yang memvalidasi nilai tidak boleh negatif (berat juga tidak boleh nol)
- Instance method: `info()` menampilkan data hewan
- Class method: `dari_dict()` sebagai factory method untuk membuat objek `Hewan` dari data berbentuk dictionary
- Static method: `validasi_jenis()` mengecek apakah jenis hewan terdaftar di klinik

### 2. LayananHewan
Menyimpan data layanan yang tersedia (perawatan, penitipan, grooming, vaksinasi).

- Atribut kelas: `total_layanan`, `biaya_admin`, `kategori_tersedia`
- Atribut instance (public): `nama_layanan`, `kategori`
- Atribut instance (private): `__harga`
- Property: `harga` dengan setter yang memvalidasi harga harus lebih dari nol
- Instance method: `tampilkan()` menampilkan detail layanan
- Class method: `ubah_biaya_admin()` mengubah atribut kelas `biaya_admin` yang berlaku untuk semua transaksi
- Static method: `validasi_kategori()` mengecek apakah kategori layanan valid

### 3. Transaksi
Menghubungkan objek `Hewan` dan `LayananHewan` dalam satu pemesanan.

- Atribut kelas: `total_transaksi`, `status_tersedia`, `nama_platform`
- Atribut instance (public): `id_transaksi`, `hewan`, `layanan`, `status`
- Atribut instance (private): `__total_bayar` (dihitung otomatis dari harga layanan ditambah biaya admin)
- Property: `total_bayar` dengan setter yang memvalidasi nilai tidak boleh negatif
- Instance method: `ubah_status()` mengubah status transaksi setelah divalidasi, dan `struk()` menampilkan ringkasan transaksi
- Class method: `batalkan()` membatalkan sebuah objek transaksi
- Static method: `validasi_status()` mengecek apakah status yang dimasukkan termasuk status yang dikenal sistem

## Cara Menjalankan

```bash
python PT1_Setriyani_2509106039.py
```

Seluruh proses pengujian sudah ditulis di bagian `if __name__ == "__main__":` sehingga cukup dijalankan langsung tanpa input manual.

## Panduan Pengujian

Saat dijalankan, program akan menampilkan secara berurutan:

1. **Data awal** - dua objek `Hewan` (satu dibuat lewat konstruktor biasa, satu lewat `dari_dict()`), dua objek `LayananHewan`, dan dua objek `Transaksi`.
2. **Uji setter valid** - mengubah umur kucing menjadi 3 dan harga grooming menjadi 80000, nilai baru berhasil tersimpan.
3. **Uji setter tidak valid** - mencoba mengubah umur menjadi -5, berat menjadi 0, dan harga menjadi -1000. Setiap percobaan ini ditolak dan program mencetak pesan peringatan tanpa mengubah nilai aslinya.
4. **Uji instance method** - `ubah_status()` dipanggil dengan status valid (`"Selesai"`) dan status tidak dikenal (`"Terbang"`) untuk membandingkan hasilnya.
5. **Uji class method** - `ubah_biaya_admin()` mengubah biaya admin untuk seluruh transaksi baru, dan `batalkan()` membatalkan transaksi yang sudah ada.
6. **Uji static method** - `validasi_jenis()`, `validasi_kategori()`, dan `validasi_status()` dipanggil langsung dari class tanpa membuat objek.
7. **Atribut kelas** - dicetak di bagian akhir untuk menunjukkan bahwa `total_hewan`, `total_layanan`, dan `total_transaksi` bertambah otomatis setiap ada objek baru.
