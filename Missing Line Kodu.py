import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

goruntu = cv2.imread('irvine_NIR.tif')
plt.hist(goruntu.ravel(),256,[0,256]); plt.show()
 
for  k in range(0,512):
	for j in range(0,512):
		if goruntu[k][j][...,0] == 0 and goruntu[k][j][...,1] == 0 and goruntu [k][j][...,2] == 0:
			goruntu[k][j] = (goruntu[k+1][j] / 2) + (goruntu[k-1][j] / 2)
cv2.imshow('duzenlenmis_goruntu' ,goruntu)
cv2.waitKey(0)
			

			
