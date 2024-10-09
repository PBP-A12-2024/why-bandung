<details>
  <summary>iii. Daftar modul yang akan diimplementasikan</summary>
1. Dashboard<br>
Features:<br>
- Navigation hub, berisi personalized data seperti recent activity, favorite products yang udah pernah di rate, dan link ke modul-modul lain.<br>
- Link-link ke product highly-rated.<br>
- Search bar yang nyambung dengan modul search system.<br><br>

Rincian regulasi aturan khusus:
- Models: Mengambil data spesifik seperti pencarian terbaru atau ulasan.
- Views: Mengambil dan memproses informasi untuk ditampilkan.
- HTML Templates: Menggunakan `base.html` agar konsisten di seluruh situs.
- Responsive Framework: Tailwind atau Bootstrap memastikan tampilan tetap ramah mobile.
- Forms: Memiliki form aksi cepat (misalnya, searchbar).
- AJAX: Update langsung untuk notifikasi atau restoran trending.
- Login Filters: Data spesifik hanya ditampilkan kepada pengguna yang sudah log in.
- Product Filtering: Menyaring restoran atau hidangan berdasarkan preferensi.

Gambaran: 
![Screenshot 2024-10-06 200918](https://github.com/user-attachments/assets/5bb7bd87-41d2-42ce-adce-534ef885d021)

2. Search System<br>
Features:
- Search system agar user dapat menelusuri berdasarkan filter yang bisa diatur, mungkin dari lokasi, menu spesifik, dll.
- Menggunakan beberapa tags untuk jenis menu ataupun cuisine.
- Results menampilkan detail restaurant dan link-link ke product pages.

Rincian regulasi aturan khusus:
- Models: Menyimpan dan mengambil data terkait restoran, menu, dan tag.
- Views: Memproses permintaan search dan return hasil yang sudah difilter.
- HTML Templates: Menggunakan template modular untuk menampilkan hasil pencarian.
- Responsive Framework: Memastikan layout pencarian ramah mobile.
- Forms: Search Form memproses query dan menampilkan hasil.
- AJAX: Memungkinkan live search suggestion tanpa memuat ulang halaman.
- Login Filters: Bisa membatasi beberapa hasil untuk pengguna yang sudah log in.
- Product Filtering: Menyaring berdasarkan tag, lokasi, atau tipe restoran.

Gambaran:
![Screenshot 2024-10-06 222203](https://github.com/user-attachments/assets/aa58c763-961f-4377-b1d5-6a9b50a6947b)

3. Product Page<br>
Features:
- Display detail-detail terkait menu atau restoran.
- Users dapat submit/edit reviews, tambahkan rating, dan hashtag.
- Karena tiap produk memiliki tag maka hal ini memudahkan modul search system dan explore and discover

Rincian regulasi aturan khusus:
- Models: Menyimpan product reviews, ratings, dan hashtags.
- Views: Mengambil product details, reviews, dan input dari user.
- HTML Templates: Terstruktur untuk menampilkan informasi product dan reviews.
- Responsive Framework: Memastikan halaman dioptimalkan untuk semua perangkat.
- Forms: Review dan rating forms, diproses oleh views.
- AJAX: Memungkinkan pengiriman reviews tanpa reload halaman.
- Login Filters: Hanya logged-in users yang bisa memberikan review dan rate.
- Product Filtering: Related products dan user reviews bisa difilter berdasarkan tags atau ratings.

Gambaran:
![Screenshot 2024-10-06 200956](https://github.com/user-attachments/assets/62e6a9e5-67ca-49ca-9b80-6145bbbfe198)

4. Location Homepage / Geomapping Interface<br>
Features:
- Map interactive yang dapat display restoran atau menu yang dapat user telusur dengan filters.
- Filters untuk searching berdasarkan kabupaten ataupun menu yang dicari.
- Berfungsi mirip dengan search system. 

Rincian regulasi aturan khusus:
- Models: Menyimpan data lokasi untuk restaurants dan menus.
- Views: Memproses permintaan untuk memfilter hasil map berdasarkan lokasi atau tags.
- HTML Templates: Menampilkan interactive map bersama dengan search filters.
- Responsive Framework: Membuat map dapat digunakan pada perangkat seluler.
- Forms: Memfilter lokasi dan menampilkan hasil yang relevan.
- AJAX: Memperbarui map secara dinamis dengan hasil pencarian baru.
- Login Filters: Lokasi atau fitur tertentu mungkin dibatasi untuk logged-in users.
- Product Filtering: Memfilter restaurants berdasarkan wilayah, tags, atau jenis cuisine.

5. Explore and Discover<br>
Features:
Memberikan suggestion kepada user terkait  restaurants atau menu yang baru ataupun trending berdasarkan user history dan rating di website.
Recommendations bisa diambil dari history user sering berinteraksi dengan tipe menu apa ataupun lokasi mana.
Memberikan highlights kepada user terkait hidden gems atau trending spots diluar search history user.

Rincian regulasi aturan khusus:
- Models: Menggunakan data user dan informasi trending restaurants.
- Views: Memproses rekomendasi berdasarkan riwayat user dan similar users.
- HTML Templates: Ditampilkan sebagai halaman terpisah atau bagian dari situs.
- Responsive Framework: Memastikan rekomendasi dapat diakses pada perangkat seluler.
- Forms: Users dapat menyaring rekomendasi dengan filters (misalnya berdasarkan jenis cuisine atau lokasi).
- AJAX: Menyediakan rekomendasi dinamis tanpa perlu memuat ulang halaman.
- Login Filters: Rekomendasi dipersonalisasi untuk logged-in users.
- Product Filtering: Menyarankan restaurants atau hidangan berdasarkan preferensi user, tren, dan tags.

Gambaran:
![Screenshot 2024-10-06 204821](https://github.com/user-attachments/assets/b13998ea-5716-487f-a6fb-09111bd7c515)


</details>
