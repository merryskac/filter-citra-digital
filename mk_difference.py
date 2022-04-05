import cv2
import numpy as np

gambar1 = cv2.imread('spbob1.jpg')
gambar2 = cv2.imread('spbob12.jpg')

g1gray = np.array(cv2.cvtColor(gambar1,cv2.COLOR_RGB2GRAY))
g2gray = np.array(cv2.cvtColor(gambar2, cv2.COLOR_RGB2GRAY))

[p1,l1] = g1gray.shape
[p2,l2] = g2gray.shape

relocate = np.zeros((p1,l1))

for i in range(p1):
    for j in range(l1):
        if g1gray[i][j]!= g2gray[i][j]:
            relocate[i][j]=0
        else:
            relocate[i][j] = g1gray[i][j]

print(relocate)
cv2.imshow('hai',np.uint8(relocate))
cv2.waitKey()


