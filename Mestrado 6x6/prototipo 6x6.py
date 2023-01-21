import copy
import csv

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from atom import ATOMClassifier
from PIL import Image

data = pd.read_csv("dataset_descriptor.csv")
print("Leu DATASET")

columns = columns = ["ip_len_mean","ip_len_median","sport_median","sport_mean","tcp_flags_mean",
"tcp_flags_median","dport_mean","dport_median","sport_rte","tcp_flags_cvq","tcp_flags_cv",
"tcp_flags_std","ip_len_cv","sport_cvq","sport_cv","ip_len_cvq","sport_std","ip_proto",
"tcp_flags_var","ip_len_std","sport_entropy","ip_len_rte","sport_var","ip_len_var",
"dport_cv","tcp_flags_rte","dport_cvq","dport_std","dport_var","dport_rte",
 "ip_len_entropy","dport_entropy","tcp_flags_entropy","Label2"]

data = data[columns]

#Transformando o target em int
for i in range(0,len(data)):
  if data.loc[i,'Label2']=="normal":
    data.loc[i,'Label2']=0
  else: #data[i,'Label2']=='attack' :
    data.loc[i,'Label2']=1
data['Label2'] = data['Label2'].astype('int64')


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
attack2 = attack.values*255
attack2=attack2
normal2 = normal.values*255
normal2=normal2

#attack2 = attack2.astype('int64')
#normal2 = normal2.astype('int64')


#CRIAÇÃO DAS IMAGENS
print("CRIA IMAGENS")
for i in range(0,len(attack2)):
  attack3 = [attack2[i]]
  attack4 =np.resize(attack3,(6,6))
  attack4 = np.array(attack4,np.uint8)
  im = Image.fromarray((attack4))
  titulo = ('./ataques6x6/ataque'+(str(i+1))+'.png')
  im.save(titulo)
  titImg = ('ataque'+(str(i+1))+'.png '+'1 0 0 5 5')
  titulo2 = ('ataques6x6/'+titImg)
  with open("./ataques6x6/ataque.txt","a+") as info:
    info.write(titulo2+"\n")
    info.read()

for i in range(0,len(normal2)):
  normal3 = [normal2[i]]
  normal4 =np.resize(normal3,(6,6))
  normal4 = np.array(normal4,np.uint8)
  im = Image.fromarray((normal4))
  titulo = ('./normal6x6/normal'+(str(i+1))+'.png')
  im.save(titulo)
  titImg = ('normal'+(str(i+1))+'.png')
  titulo2 = ('normal6x6/'+titImg)
  with open("./normal6x6/normal.txt","a+") as bg:
    bg.write(titulo2+"\n")
    bg.read()
