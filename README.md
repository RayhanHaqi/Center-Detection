# Center-Detection

line 6 = video capture dari webcam
line 7-14 = buat window berisi trackbar untuk mengatur range warna benda yang ingin dideteksi
line 17 = frame dari video capture
line 18 = menyimpan nilai koordinat titik tengah frame(line 17) untuk digunakan nanti
line 19 = convert frame (line 17) BGR to HSV
line 20-25 = menyimpan nilai dari trackbar(line 7-14)
line 27 = bikin frame yang berisi frame(line 19) hanya dengan range warna yang ditentukan
line 29 = mengambil bagian dari frame(line 19) dengan bentuk dari frame(line 27)
line 30 = frame(line 29) diubah ke greyscale
line 31 = frame(line 30) diblur
line 33 = membuat frame binary dari frame(line 30)
line 38 = membuat lingkaran di tengah-tengah frame(line 17) dengan titik koordinat dari (line 18)
line 43 = menyimapan nilai garis-garis kontur pada frame binary(line 33)
line 45-54 = membuat looping untuk menggambar kontur yang luas areanya lebih dari 4000, membuat kotak pembatas boundingRectangle, membuat titik tengah dari kontur, dan mendeteksi jika titik tengah kontur mendekati titik tengah frame.
line 56 = menampilkan frame yang sudah digambar-gambar
