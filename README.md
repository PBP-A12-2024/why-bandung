<h2>WhyBandung</h2>
<p>
  Daftar Anggota
  <ul>
    <li>Farrel Dharmawan Dwiyudanto - 2306275506</li>
    <li> Najya Johara Robby - 2306245674/li>
    <li>Hubban Syadid - 2306165830</li>
    <li>Muhammad Fadhil Nur Aziz - 2306275531</li>
    <li>Karina Maharani - 2306165736</li>
  </ul>
</p>

<details>
  <summary>i. Deskripsi Singkat</summary>
Pernahkah Anda kesulitan untuk menemukan restoran yang anda inginkan selama berjalan-jalan di kota bandung, atau kesulitan mencari tempat kuliner yang menyediakan makanan minuman khas bandung?
  <br><br>
WhyBandung hadir untuk membantu baik wisatawan maupun warga lokal dalam menemukan kuliner terbaik di Bandung. Situs ini dilengkapi dengan sistem navigasi berbasis peta yang unik dan intuitif, sehingga memudahkan pengguna mencari makanan dan minuman yang diinginkan. WhyBandung memungkinkan pengguna untuk mengeksplorasi kuliner di berbagai wilayah berdasarkan lokasi atau kategori makanan. Selain itu, WhyBandung akan terus mengembangkan dan memperbarui daftar lokasi kuliner secara berkala.\
  <br><br>
Tim A12SITEK memilih Kota Bandung karena dikenal sebagai kota wisata yang populer dengan ragam kuliner yang khas. Namun, terdapat kekurangan dalam sistem navigasi kuliner di Bandung. Wisatawan sering kali tidak mengetahui kuliner khas di suatu daerah karena sistem pencarian aplikasi seperti Google Maps mengharuskan pengguna untuk mencari makanan secara spesifik. Akibatnya, wisatawan cenderung mengunjungi tempat-tempat kuliner yang sudah terkenal, sehingga melewatkan kedai-kedai lokal yang lebih autentik. Padahal, kuliner lokal memberikan pengalaman yang lebih khas dan mendalam terhadap budaya suatu daerah. Inilah yang mendorong kami untuk mengembangkan WhyBandung.

</details>

<details>
  <summary>ii. Daftar modul yang akan diimplementasikan</summary>
1. Dashboard<br>
  Section Home<br>
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
  Section Profil

  Section Profile<br>
  Features:<br>
- Journal Entry. User mengupload cerita terkait pengalaman mereka dengan beberapa tempat<br>
- Link-link ke lokasi yang ada di journal entry and associated review/entry made by user at halaman produk toko.<br><br>

Rincian regulasi aturan khusus:
- Models: Menyimpan product reviews, ratings, dan hashtags.
- Views: Mengambil product details, reviews, dan input dari user.
- HTML Templates: Terstruktur untuk menampilkan informasi product dan reviews.
- Responsive Framework: Memastikan halaman dioptimalkan untuk semua perangkat.
- Forms: Review dan rating forms, diproses oleh views.
- AJAX: Memungkinkan pengiriman reviews tanpa reload halaman.
- Login Filters: Hanya logged-in users yang bisa memberikan review dan rate.
- Product Filtering: Related products dan user reviews bisa difilter berdasarkan tags atau ratings.
  
CRUD
- CREATE: Membuat Journal Entry (reviews, tambahkan rating, dan tag) di Dashboard section profil
- READ : Mengambil data sejarah Jurnal Pengguna.
- UPDATE: Mengubah isi Jurnal Entry.
- DELETE: Menghapus sebuah Jurnal Entry.

Gambaran: 
![Screenshot 2024-10-06 200918](https://github.com/user-attachments/assets/5bb7bd87-41d2-42ce-adce-534ef885d021)

2. What to Eat?<br>
Features:
- Display tinder like form to find what current food should be made.
- Users dapat mengisi form dan program membuat flowchart untuk memberikan rekomendasi makanan.
- Karena tiap produk memiliki tag maka hal ini memudahkan modul ini untuk memberi rekomendasi makanan.

Rincian regulasi aturan khusus:
- Models: Form untuk menerima hasil swipe user.
- Views: Mengambil hasil swiping sebagai bentuk input user, dan tampilkan hasil.
- HTML Templates: Terstruktur untuk menampilkan swiping interface.
- Responsive Framework: Memastikan halaman dioptimalkan untuk semua perangkat.
- Forms: Hasil isi swipe form.
- Login Filters: Hanya logged-in users yang bisa memberikan review dan rate.

CRUD
- CREATE: Membuat rekomendasi makan serta toko associated user.
- READ : Memnampilkan history hasil isi form rekomendasi makan, mengambil sejarah makan user.
- UPDATE: Mengubah hasil swipe sebelum submit jika user menginginkan.
- DELETE: Menghapus item dari history rekomendasi makan user.

3. Product Page<br>
Features:
- Display detail-detail terkait menu atau restoran.
- Users dapat submit/edit journal entry (reviews, tambahkan rating, dan tag). 
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

CRUD
- CREATE: Membuat Journal Entry (reviews, tambahkan rating, dan tag) di Dashboard section profil
- READ : Mengambil data sejarah Jurnal Pengguna, Mengambil data product.
- UPDATE: Mengubah isi Jurnal Entry, Mengubah hasil ratings pada product page setelah submit journal entry.
- DELETE: Menghapus sebuah Jurnal Entry.

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

CRUD
- CREATE: Membuat Planner Perjalanan dan toko yang ingin divisit
- READ : Mengambil data toko per lokasi kabupaten di map.
- UPDATE: Mengubah Planner Perjalanan dan toko yang ingin divisit.
- DELETE: Menghapus sebuah Jurnal Entry.

5. Penambahan Toko (ONLY FOR ADMIN)
Features:
- Add new stores and products to database.
- Modify pre-existing stores as well products (Update or delete)

Rincian regulasi aturan khusus:
- Models: Membuat model toko.
- Views: Memproses menambah atau mengubah toko atau produk.
- HTML Templates: Menampilkan all stores and products secara tabular.
- Forms: Memfilter lokasi dan menampilkan hasil yang relevan.
- Product Filtering: Memfilter restaurants berdasarkan wilayah, tags, atau jenis cuisine.

CRUD
- CREATE : Membuat toko baru dan menambah produk.
- READ : Menampilkan toko dan produk yang sudah ada.
- UPDATE : Mengubah toko dan produk yang sudah ada.
- DELETE : Menghapus toko dan produk yang sudah ada.

NON CRUD FEATURES YANG MUNGKIN DIIMPLEMENTASIKAN JIKA WKAKTU MEMUNGKINKAN<br>
1. Search System<br>
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

2. Explore and Discover<br>
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

<details>
  <summary>iiI. Deskripsi Dataset</summary>
Dalam pembuatan web aplikasi WhyBandung, kami membutuhkan database yang memiliki data mengenai informasi seputar produk kuliner yang berada di kota Bandung. Data ini kami dapatkan melalui pencarian di internet. Data yang akan kami gunakan ini berfungsi untuk mempermudah pengguna aplikasi WhyBandung untuk menemukan makanan ataupun minuman berdasarkan lokasi, kategori produk, harga produk, dan toko yang menyediakan produk tersebut. Pada dataset kami terdapat kolom Kode Produk, Nama Produk, Kategori, Toko, Harga Retail, dan Lokasi untuk memberikan informasi detail yang dibutuhkan pengguna nanti.
  <br><br>
Kolom Kode Produk digunakan sebagai kode unik untuk setiap item produk, sehingga aplikasi dapat dengan mudah membedakan satu produk dengan produk lainnya. Kolom Nama Produk digunakan untuk memberikan informasi nama produk spesifik yang dapat dicari oleh pengguna. Lalu, terdapat kolom Kategori yang digunakan untuk mengelompokkan produk berdasarkan kategorinya yang seusai contohnya seperti kategori kue, minuman, makanan berat, dan lain-lain. Selain mengelompokkan produk, Kolom Kategori dapat membantu pengguna untuk mencari suatu produk berdasarkan kategori produk tersebut. Kolom Toko digunakan untuk memberikan informasi mengenai tempat atau kedai apa yang menjual produk tersebut sehingga pengguna dapat mengetahui dimana pengguna dapat membeli produk yang diinginkan.
  <br><br>
Kolom Harga Retail memberikan informasi mengenai harga suatu produk sehingga pengguna dapat memilih produk yang mereka inginkan sesuai dengan budget yang mereka miliki. Sedangkan kolom Lokasi digunakan untuk memberikan informasi pada daerah mana produk tersebut berada. Pengguna juga dapat mencari produk sesuai dengan lokasi yang diinginkan.
<br><br>
DATABASE DAPAT DIAKSES MELALUI LINK INI : https://docs.google.com/spreadsheets/d/1peBfLmwdaHBPClgn3gGGbBMKNjFn44a-ky20q7FM3h8/edit?usp=sharing 

</details>

<details>
  <summary>iv. Deskripsi Jenis User dan Wewenang</summary>
1. Dashboard
User Biasa:
- Bisa melihat recent activity seperti pencarian terbaru atau ulasan yang pernah dibuat.
- Melihat favorite products atau restoran yang sudah pernah di-review atau diberi rating.
- Akses ke link highly-rated products berdasarkan preferensi mereka.
- Gunakan search bar untuk menelusuri produk atau restoran.
Developer:
- Sama seperti User Biasa, tapi ditambah kemampuan untuk melihat data terkait produk atau restoran seperti tren, statistik rating, dan aktivitas user lainnya.
- Akses ke modul developer untuk pengelolaan produk dan restoran.
- Bisa menambah link ke fitur lain yang hanya diakses oleh developer, seperti manajemen user, monitoring ulasan, dan pengelolaan sistem.
  
2. What to Eat?
User Biasa:
- Bisa mengisi form untuk melihat rekomendasi makanan.
- User bisa gacha makanan untuk seru-seruan atau jika tidak tahu mau makan apa.
Developer:
- Developer dapat memodifikasi algoritma rekomendasi, termasuk bagaimana tag makanan digunakan untuk mencocokkan makanan dengan preferensi pengguna.
- Developer memiliki akses ke alat admin lanjutan, seperti mengelola tag makanan, kategori, dan memonitor aktivitas pengguna terkait rekomendasi.
   

3. Product Page
User Biasa:
- Bisa melihat detail produk atau restoran, seperti nama restoran, menu yang tersedia, dan ulasan dari user lain.
- Bisa memberikan ulasan dan rating pada produk atau restoran, dengan menambahkan hashtag untuk memudahkan pencarian.
- Akses ke produk terkait yang difilter berdasarkan tag atau rating.
Developer:
- Sama dengan User Biasa, tetapi developer bisa mengedit dan menghapus produk atau ulasan.
- Bisa melakukan moderasi pada ulasan yang diberikan user.
  
4. Location Homepage / Geomapping Interface
User Biasa:
- Bisa melihat peta interaktif yang menunjukkan lokasi restoran atau menu berdasarkan filter seperti lokasi atau jenis masakan.
- Dapat melakukan pencarian berbasis lokasi geografis dan filter sesuai preferensi mereka.
- Akses terbatas hanya untuk data restoran yang sudah dipublikasikan atau tersedia untuk umum.
- Developer:
- Selain semua fitur yang dimiliki User Biasa, developer bisa mengelola data lokasi restoran.
- Bisa menambah atau memperbarui informasi lokasi langsung dari peta interaktif.

5. Penambahan Toko
User Biasa:
- Tidak bisa Akses
Developer:
- Dapat menambah, melihat, memodifikasi dan menghapus toko


</details>
