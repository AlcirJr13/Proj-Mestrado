import copy
import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import cv2
from PIL import Image

data = pd.read_csv("dataset_descriptor.csv")
print("Leu DATASET")

#print(attack)
#print(normal)
#print(data.columns)
#print(data.shape)
#print(data.dtypes)

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

columnsAttack = data.columns.values
columnsNormal = data.columns.values

attack = []
attack = pd.DataFrame(data=attack, columns=columnsAttack)
normal = []
normal = pd.DataFrame(data=normal,columns=columnsNormal)


print("Separação atk norm")
#for i in range(0,len(data)):
for i in range(0,50):
  if data.loc[i,'Label2']=="normal":
    normal.loc[len(normal)] = data.loc[i]
  else: #data[i,'Label2']=='attack' :
    attack.loc[len(attack)] = data.loc[i]
  #print(i)



attack = attack.drop(columns=['Label2'])

normal = normal.drop(columns=['Label2'])



print("transformação int")
attack2 = attack.values
attack2=attack2*1000000000
normal2 = normal.values
normal2=normal2*1000000000


attack2 = attack2.astype('int64')
normal2 = normal2.astype('int64')


attack2 = attack2%255
normal2 = normal2%255

teste=np.random.randint(0,256, 24*24) #CRIANDO MATRIZ 1-D ALEATÓRIA DE TESTE COM 576 Nº
print(teste)
print("########################")
teste.resize((24,24)) # TRANSFORMANDO EM MATRIZ 24 X 24
print(teste.shape)

# print("CRIA IMAGENS")
# for i in range(0,len(teste)):
#   teste2 = teste
#   teste2 = np.array(teste2,np.uint8)
#   im = Image.fromarray((teste2))
#   titulo = ('./ataques/ataque'+(str(i+1))+'.png')
#   im.save(titulo)
#   titImg = ('ataque'+(str(i+1))+'.png '+'1 0 0 32 0')
#   titulo2 = ('/ataques/'+titImg)
#   with open("./ataques/ataque.txt","a+") as info:
#     info.write(titulo2+"\n")
#     info.read()

# print("CRIA IMAGENS")
# for i in range(0,len(attack2)):
#   attack3 = [attack2[i]]
#   attack3 = np.array(attack3,np.uint8)
#   im = Image.fromarray((attack3))
#   titulo = ('./ataques/ataque'+(str(i+1))+'.png')
#   im.save(titulo)
#   titImg = ('ataque'+(str(i+1))+'.png '+'1 0 0 32 0')
#   titulo2 = ('/ataques/'+titImg)
#   with open("./ataques/ataque.txt","a+") as info:
#     info.write(titulo2+"\n")
#     info.read()


# for i in range(0,len(normal2)):
#   normal3 = [normal2[i]]
#   normal3 = np.array(normal3,np.uint8)
#   im = Image.fromarray((normal3))
#   titulo = ('./normal/normal'+(str(i+1))+'.png')
#   im.save(titulo)
#   titImg = ('normal'+(str(i+1))+'.png')
#   titulo2 = ('/normal/'+titImg)
#   with open("./normal/normal.txt","a+") as bg:
#     bg.write(titulo2+"\n")
#     bg.read()


#for i in range(0,len(X2)):
#  X3 = [X2[i]]
#  X3 = np.array(X3,np.uint8)
#  im = Image.fromarray((X3))
#  titulo = ('./imagens/Linha'+str(i)+'.png')
#  im.save(titulo)



#print('======NORMAL======')
#print(attack)
#print('======MODIFICADA======')
#print(y.head())
#X2 = attack.values
#X2=X2*10000000000000000000
#print(X2)
#X2 = X2.astype(int)
#print('======INTEIRO======')
#print(X2)
#X2 = X2%255
#print('======FINAL======')
#print(X2)
#print('======Y======')
#print(y)


#X2 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254],
#          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254],
#          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254]]