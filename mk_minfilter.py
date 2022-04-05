import cv2
import numpy as np

#membaca gambar
image = cv2.imread('spbob_saltpepper.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#relokasi gambar pada matriks yang baru sehingga memiliki frame hitam 1px
[panjang,lebar]=np.shape(gray)
relocate = np.zeros((panjang+2,lebar+2))
[t_pan,t_leb] = np.shape(relocate)

#matriks tempat gambar hasil akhir filter
template =np.zeros((panjang,lebar))

#menyimpan piksel agar dapat dilakukan perhitungan
pixels=[]
rata = 0

# menyalin piksel gambar ke relocate
for i in range(1,t_pan-1):
    for j in range(1,t_leb-1):
        relocate[i][j] = int(gray[i-1][j-1])

#operasi pengambilan piksel dan diambil rata-ratanya
for i in range(1,t_pan-1):
    for j in range(1,t_leb-1):
        for k in range(-1,2):
            for l in range(-1,2):
                pixels.append(np.uint8(relocate[i-k][j-l]))

        # dicari min dari nilai piksel
        pixel = min(pixels)
        template[i-1][j-1]=pixel
        pixels.clear()
#ubah ke tipe data uint88 agar nilai piksel konstan 0-255
relocate = np.uint8(relocate)
template = np.uint8(template)
print(template)

#menampilkan window
cv2.imshow('Min Filter',template)
cv2.imshow('Sebelum',gray)
cv2.waitKey()

