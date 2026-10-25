# Introduction

Searching Algorithm (Algoritma Pencarian) adalah kumpulan metode untuk menemukan jalur dari titik awal menuju tujuan. Proyek ini menampilkan proses pencarian jalur pada labirin acak secara visual, sehingga cara kerja setiap algoritma dapat diamati dan dibandingkan.

Labirin dibuat secara acak menggunakan metode recursive backtracker. Titik awal berada di kiri atas dan titik tujuan di kanan bawah. Tersedia tiga algoritma pencarian:

1. **Depth-First Search (DFS)** menelusuri satu cabang sedalam mungkin sebelum mencoba cabang lain.
2. **Breadth-First Search (BFS)** menelusuri labirin lapis demi lapis menggunakan antrean. Karena setiap langkah memiliki biaya yang sama, BFS menemukan jalur dengan jumlah langkah paling sedikit.
3. **A\*** memprioritaskan sel berdasarkan jarak yang sudah ditempuh dan estimasi jarak ke tujuan menggunakan heuristik Manhattan.

# Requirement

1. Python 3
2. Tkinter, yang biasanya sudah termasuk dalam instalasi Python. Pastikan instalasi Python yang digunakan mendukung Tk.

Program hanya menggunakan library bawaan Python, sehingga tidak memerlukan instalasi library eksternal. Pada Linux, Tkinter mungkin perlu dipasang terpisah melalui package manager sistem operasi.

# How To use

1. Buka terminal di folder `Searching Algorithm`.
2. Jalankan salah satu visualisasi berikut:

   ```bash
   python DFS.py
   ```

   ```bash
   python A_star.py
   ```

   ```bash
   python BFS.py
   ```

3. Atur ukuran labirin melalui slider **Maze Size (N × N)**. Ukuran awal adalah 40 × 40; nilai yang tersedia adalah bilangan genap dari 2 hingga 200.
4. Atur kecepatan animasi melalui slider **Animation Speed** (1–100).
5. Klik **Solve (DFS)**, **Solve (BFS)**, atau **Solve (A*)** untuk membuat labirin acak dan menjalankan algoritma terkait.
6. Gunakan **Pause** atau **Resume** untuk menjeda atau melanjutkan animasi. Klik **Stop/Reset** untuk menghentikan pencarian dan membersihkan tampilan eksplorasi.

# Running/Result

Jendela visualisasi menampilkan labirin, titik awal, titik tujuan, dan proses penelusuran. Warna sel pada animasi:

- Biru muda: sel yang menunggu untuk dieksplorasi.
- Abu-abu: sel yang sudah dieksplorasi.
- Oranye: sel yang sedang diperiksa.
- Ungu: persimpangan atau cabang labirin.
- Merah: jalur akhir dari titik awal ke tujuan.

Setelah pencarian selesai, aplikasi menampilkan jumlah langkah pada jalur, jumlah ekspansi, waktu pencarian, dan status penyelesaian. DFS tidak selalu menemukan jalur terpendek, sedangkan BFS dan A* menggunakan pendekatan yang menjamin jalur terpendek untuk labirin ini.

![Tampilan Maze Solver Visualizer](https://github.com/user-attachments/assets/3fdc6352-4e60-4142-a760-752c9d122ca7)

Jalankan `DFS.py`, `BFS.py`, dan `A_star.py` secara terpisah untuk membandingkan urutan eksplorasi dan jalur yang ditemukan oleh masing-masing algoritma.
