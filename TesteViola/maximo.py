import copy
import csv

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from atom import ATOMClassifier
from PIL import Image

data = pd.read_csv("D:\Documentos\Mestrado\Projeto\dataset_3.csv")
print("Leu DATASET")


columnsAttack = data.columns.values
columnsNormal = data.columns.values

attack = []
attack = pd.DataFrame(data=attack, columns=columnsAttack)
normal = []
normal = pd.DataFrame(data=normal,columns=columnsNormal)


print("Separação atk norm")
for i in range(0,len(data)):
#for i in range(0,100):
  if data.loc[i,'Label2']==0:
    normal.loc[len(normal)] = data.loc[i]
  else: #data2[i,'Label2']==1 :
    #print("ATAQUE", i)
    attack.loc[len(attack)] = data.loc[i]
  print(i)



attack = attack.drop(columns=['Label2'])
normal = normal.drop(columns=['Label2'])

#TRANFORMAR FEATURES EM INT
print("transformação int")
attack2 = ((attack.values)/45499)
attack2 = attack2*255
#attack2=attack2*1000000000000000

normal2 = ((normal.values)/45499)
normal2 = normal2*255
#normal2=normal2*1000000000000000

attack2 = attack2.astype('int64')
normal2 = normal2.astype('int64')
# print("attack\n", attack2)
# print("normal\n", normal2)

print(attack2)

#maxi = data.max()
#print(data)
#print(maxi)
#print(maxi.max())