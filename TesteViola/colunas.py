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

columns = ["ip_proto","ip_len_mean","ip_len_median","ip_len_var",
               "ip_len_std","ip_len_entropy","ip_len_cv","ip_len_cvq",
               "ip_len_rte", "sport_mean","sport_median","sport_var","sport_std",
               "sport_entropy","sport_cv","sport_cvq","sport_rte",
               "dport_mean","dport_median","dport_var","dport_std",
               "dport_entropy","dport_cv","dport_cvq","dport_rte",
               "tcp_flags_mean","tcp_flags_median","tcp_flags_var",
               "tcp_flags_std","tcp_flags_entropy","tcp_flags_cv",
               "tcp_flags_cvq","tcp_flags_rte", "Label2"]

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
  #print(i)


attack = attack.drop(columns=['Label2'])
normal = normal.drop(columns=['Label2'])

#TRANFORMAR FEATURES EM INT
print("transformação int")
attack2 = attack.values
attack2=attack2*1000000000000000
normal2 = normal.values
normal2=normal2*1000000000000000

attack2 = attack2.astype('int64')
normal2 = normal2.astype('int64')


# #TRANSFORMAR VALORES ENTRE 0 E 255 (TONS DE CINZA)
attack2 = attack2%255
normal2 = normal2%255


attack3 = attack2[0:1500]
attack4 = attack2[1500:3000]
attack5 = attack2[3000:4500]
attack6 = attack2[4500:6000]
attack7 = attack2[6000:7500]

attackT3 = attack3.transpose()
attackT4 = attack4.transpose()
attackT5 = attack5.transpose()
attackT6 = attack6.transpose()
attackT7 = attack7.transpose()

attack8 = np.array(attackT3,np.uint8)
im = Image.fromarray((attack8))
im.save('./1-Ataque.png')

attack9 = np.array(attackT4,np.uint8)
im = Image.fromarray((attack8))
im.save('./2-Ataque.png')

attack10 = np.array(attackT5,np.uint8)
im = Image.fromarray((attack9))
im.save('./3-Ataque.png')

attack11 = np.array(attackT6,np.uint8)
im = Image.fromarray((attack11))
im.save('./4-Ataque.png')

attack12 = np.array(attackT7,np.uint8)
im = Image.fromarray((attack11))
im.save('./5-Ataque.png')

normal3 = normal2[0:1500]
normal4 = normal2[1500:3000]
normal5 = normal2[3000:4500]
normal6 = normal2[4500:6000]
normal7 = normal2[6000:7500]

normalT3 = normal3.transpose()
normalT4 = normal4.transpose()
normalT5 = normal5.transpose()
normalT6 = normal6.transpose()
normalT7 = normal7.transpose()

normal8 = np.array(normalT3,np.uint8)
im = Image.fromarray((normal8))
im.save('./1-Normal.png')

normal9 = np.array(normalT4,np.uint8)
im = Image.fromarray((normal8))
im.save('./2-Normal.png')

normalnormal10 = np.array(normalT5,np.uint8)
im = Image.fromarray((normal9))
im.save('./3-Normal.png')

normal11 = np.array(normalT6,np.uint8)
im = Image.fromarray((normal11))
im.save('./4-Normal.png')

normal12 = np.array(normalT7,np.uint8)
im = Image.fromarray((normal11))
im.save('./5-Normal.png')