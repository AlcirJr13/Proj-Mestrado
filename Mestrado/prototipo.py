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


#Utilizando modelo ATOM para geração de novas características
# https://towardsdatascience.com/deep-feature-synthesis-vs-genetic-feature-generation-6ba4d05a6ca5

# https://tvdboom.github.io/ATOM/v4.13/API/ATOM/atomclassifier/

#atom = ATOMClassifier(data, y="Label2", n_rows=1e3, verbose=2)
atom = ATOMClassifier(data, y="Label2", n_rows=1, verbose=2)
#atom.impute()
#atom.encode()

#Deep Feature Synthesis - DFS
print("============================DFS=======================")
atom.branch="dfs"

atom.feature_generation(
    strategy="dfs",
    n_features=543,
    verbose=1,
    operators=["add", "mul"],
)

#print("======DFS======")
#print(atom.dataset.head())

data2=atom.dataset
#print("data2\n", data2)

columnsAttack = data2.columns.values
columnsNormal = data2.columns.values

attack = []
attack = pd.DataFrame(data=attack, columns=columnsAttack)
normal = []
normal = pd.DataFrame(data=normal,columns=columnsNormal)

print("Separação atk norm")
for i in range(0,len(data2)):
#for i in range(0,100):
  if data2.loc[i,'Label2']==0:
    normal.loc[len(normal)] = data2.loc[i]
  else: #data2[i,'Label2']==1 :
    #print("ATAQUE", i)
    attack.loc[len(attack)] = data2.loc[i]
  #print(i)


attack = attack.drop(columns=['Label2'])
normal = normal.drop(columns=['Label2'])

#TRANFORMAR FEATURES EM INT
print("transformação int")
attack2 = attack.values
attack2 = attack2


normal2 = normal.values
normal2 = normal2


#attack2 = attack2.astype('int64')
#normal2 = normal2.astype('int64')


#CRIAÇÃO DAS IMAGENS
print("CRIA IMAGENS")
for i in range(0,len(attack2)):
  attack3 = [attack2[i]]
  attack4 =np.resize(attack3,(24,24))
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
