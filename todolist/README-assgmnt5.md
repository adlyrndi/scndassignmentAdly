**Tugas 5 PBP**

**Adly Renadi Raksanagara**
**/ 2106752306**
**/ PBP A**

1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
> Jawab : 
> 
>->Pengertian dari **INTERNAL CSS** sendiri adlaah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain. 
> 
>Internal CSS juga memiliki kelebihan yaitu tidak perlu mengupload beberapa file karena HTML dan CSS nya berada dalam satu file, Selain itu juga Class dan ID bisa digunakan oleh internal stylesheet dan juga perubahan pada internal CSS hanya berlaku pada satu halaman saja. Namun internal CSS juga memiliki kekurangan yaitu ketidak efisienan apabila ingin menggunakan CSS yang sama dalam beberapa file.

  
  
>->sedangkan EXTERNAL CSS adalah kode CSS yang ditulis terpisah dengan kode HTML yang dimana ditulis dalam sebuah file yang b erekstensi .css. File external CSS juga biasannya diletakkan setelah bagian <head> pada halaman.
>
> External CSS juga memiliki kelebihan yaitu ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jauh lebih rapih. Selain itu juga loading website akan menjadi lebih cepat dan file CSS dapat digunakan dalam beberapa halaman website sekaligus.
>
> Namun External CSS memiliki kekurangan yaitu, halaman akan menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML.
 
  
> -> Yang terakhir ada INLINE CSS yang  dimana ia adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiapelemen HTML memiliki atribut style dan disitulah inline CSS ditulis. Inline CSS memiliki kelebihan yaitu, Sanmgat membantu ketika ingin menguji dan melihat perubahan pada satu elemen, berguna untuk memperbaiki kode denghan cepat, dan Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat. Namun ia memiliki kekuranggan yaitu, Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML

  
2.Jelaskan tag HTML5 yang kamu ketahui.
  >Jawab:
  > `<button>` untuk membuat buttonn yang dapat di klik ; `<h1> s/d <h6>` Membuat judul atau heading ; `<hr>` Memisahkan konten (biasanya ditampilkan garis pembatas) ;  `<p>` membuat paragraf ; `<strong>` Membuat teks penting ; `<img>` Elemen untuk mendefinisikan gambar ; dll
  
3. Jelaskan tipe-tipe CSS selector yang kamu ketahui!
  > Jawab : 
  >1. Selektor Tag : misal ada elemen `<p>` ; `P{ color : red; }`
  >2. Selektor Class : misal ada class home ; `.home{ color: red; \n background : white;}`
  >3. Selektor ID : menggunakan kode pagar `#` ; `#header{color : red \n background : blue;}`
  >4. Selektor Atribut : selektor yang memilik elemen berdasarkan atribut ; `input[type=text]{background : none; /n color : blue}` 
  >5. Selektor Universal : elektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu. ; `* { border: 1px solid grey;}` 
  >6. Selektor pseudo : yang terdiri dari dua macam, yaiotu pseudo class dan pseudo element ; `selektor:psudo-class {/* isi*/} seperti a:hover {color: green;}` & pseudo element `p span {color: magenta;}`
  
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
  >jawab :
  > membuat styling dan juga menbuat halamman menjadi responseive dengan menambhakan `<meta name="viewport" content="width=device-width, initial-scale=1.0">` dan juga memanfaatkan media query
  
