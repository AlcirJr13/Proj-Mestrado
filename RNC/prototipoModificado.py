import copy
import csv

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from atom import ATOMClassifier
from PIL import Image

data = pd.read_csv("D:/Documentos/Alcir Jr/Mestrado/Projeto/dataset_3.csv")
print("Leu DATASET")

data = data.drop(columns=['Unnamed: 0'])

#Embaralhar linhas do data
data = data.sample(frac=1)

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
attack2 = (attack.values)*255
attack2 = attack2


normal2 = (normal.values)*255
normal2 = normal2


#attack2 = attack2.astype('int64')
#normal2 = normal2.astype('int64')


#CRIAÇÃO DAS IMAGENS
print("CRIA IMAGENS")
for i in range(0,len(attack2)):
  if i < 8956:
    attack3 = [attack2[i]]
    attack4 =np.resize(attack3,(6,6))
    attack4 = np.array(attack4,np.uint8)
    im = Image.fromarray((attack4))
    titulo = ('./ataques/ataque'+(str(i+1))+'.png')
    im.save(titulo)
    titImg = ('ataque'+(str(i+1))+'.png '+'1 0 0 23 23')
    titulo2 = ('ataques/'+titImg)
    with open("./ataques/ataque.txt","a+") as info:
      info.write(titulo2+"\n")
      info.read()

for i in range(0,len(normal2)):
  normal3 = [normal2[i]]
  normal4 =np.resize(normal3,(24,24))
  normal4 = np.array(normal4,np.uint8)
  im = Image.fromarray((normal4))
  titulo = ('./normal/normal'+(str(i+1))+'.png')
  im.save(titulo)
  titImg = ('normal'+(str(i+1))+'.png')
  titulo2 = ('normal/'+titImg)
  with open("./normal/normal.txt","a+") as bg:
    bg.write(titulo2+"\n")
    bg.read()
