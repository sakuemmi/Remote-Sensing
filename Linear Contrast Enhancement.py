import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('Irvine_TM_B1.tif',0)
img1 = cv2.imread('Irvine_TM_B2.tif',0)
img2 = cv2.imread('Irvine_TM_B3.tif',0)
img3 = cv2.imread('Irvine_TM_B4.tif',0)
equ = cv2.equalizeHist(img)
equ1 = cv2.equalizeHist(img1)
equ2 = cv2.equalizeHist(img2)
equ3 = cv2.equalizeHist(img3)
cv2.imwrite('resa.tif',equ)
cv2.imwrite('res1a.tif',equ1)
cv2.imwrite('res2a.tif',equ2)
cv2.imwrite('res3a.tif',equ3)
