import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

b1=plt.imread("L7_TM_Band1.tif",0)            
b2=plt.imread("L7_TM_Band2.tif",0)
b3=plt.imread("L7_TM_Band3.tif",0)
b4=plt.imread("L7_TM_Band4.tif",0)
b5=plt.imread("L7_TM_Band5.tif",0)
b7=plt.imread("L7_TM_Band7.tif",0)


def to_white(b):                              
    for i in range(len(b)):
       for j in range(len(b[1])):
            if b[i][j]==0:
                b[i][j]=255
    return b

def a_duz(b):                                       
    return b-b.min()

list_b=[b1,b2,b3,b4,b5,b7]              
list_i=["Band1_atm_duz.tif","Band2_atm_duz.tif","Band3_atm_duz.tif","Band4_atm_duz.tif","Band5_atm_duz.tif","Band7_atm_duz.tif"]                          
s=0
for i in list_b:
    Image.fromarray(a_duz(to_white(i))).save(list_i[s])
    s+=1

quit()
