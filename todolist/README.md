Pertanyaan dalam Penugasan 4 PBP
>Oleh : Adly Renadi


1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form> ?
  >Jawab : CSRF adalah sebuah serangan yang membuat pengguna internet  tanpa sadar mengirimkan request (permintaan) kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan. Sehingga, aplikasi tersebut mengeksekusi suatu tindakan yang sebenarnya tidak dikehendaki oleh pengguna internet. Contohnya adalah menghapus akun secara permanen, atau metransfer uang ke suatu akun.
  
  >Maka dari itu, {% csrf_token %} memiliki kegunaan untuk mencegah serangan crsf yang mungkin terjadi. Sehingga apabila tidak ada {% csrf_token %} tersebut didalah <form> mungkin saja ada serangan CSRF dapat terjadi dan ketika serangan tersebut berhasil berhasil , resiko yang didapat bisa sangat besar seperti kehilangan akun dan lain sebgainnya.
  
 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
  >jawab : Ya, bisa, kita dapat membuat elemn <form> secara manual tanpa menggunakan generator dengan cara di dalam file html membuat tag <form> yang dimana di dalam tag tersebut akan memiliki dua atribut yaitu action dan method.
  
  
 3.Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML!
  > Jawab : Pada data yang di submisi melalui HTML form menggunakan line of code yang terdapat di file views.py dan akan disimpan ke dalam database menggunakan code yagn terdapat di models.py. Setelah itu, data data tersebut akan ditampilkan dalam bentuk HTML dengan menggunakan fungsi show_todolist yang ada di dalam file views.py  dan di dalam html aka ada looping dari list_of_task ayng berisikan task dari pengguna sesuai filteran.
  
  > Setelah itu, Dari sisi user, nanti user akan membuat akun terlebih dahulu jika belum mempunyai akun dan memsukan data data yagn diperlukan yang dimana juga data data tersebut akan dimasukan ke dalam databse. Setelah membuat akun user akan mencoba login dan ketika username dan password dimasukan akan langsung mencocokan ke database apakah sudah sesuai atau belum, jika sudah user akan langusng dialihkan kehalaman todolist. Setelah di halamn todolist user dapat membuat task baru yang nantinya akna dialikan juga ke halaman baru newtask dan user jgua dapat menghapus dan mengubah statusnya menjado selesai

  4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
  >Jawab : pertama, kita membuat sebuah aplikasi todolist dengan perintah python manage.py startapp todolist. Setelah itu kita melengkapi semua fungsi yang akan dibuat di views.py dan langusng menambahkan path di urls.py yang harus kita buat filenya. Setelah itu lengkapi juga models di models.py yang berisi data data sepert, date, user, description, dll. Setelah itu kita melengkapi file html yang akan dibuat seperti todolist.html, login.htnml, register.html, dll. Setelah semuannya terconnect dan melakukan routing pada urls.py dengan setiap funsgi di views.py melakukan tahap push ke repo dan jug adeployment ke heroku
