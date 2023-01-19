import cv2
import numpy as np
import random

def imagem_horizontal():
  x = random.randint(1,22400)
  des_img = ('ataques6x6/ataque'+(str(x))+'.png')
  #des_img = ('normal/normal'+(str(x))+'.png')
  img1 = cv2.imread(des_img)
  x = random.randint(1,22400)
  #des_img = ('ataques/ataque'+(str(x))+'.png')
  des_img = ('normal6x6/normal'+(str(x))+'.png')
  img2 = cv2.imread(des_img)

  hori = np.concatenate((img1, img2), axis=1)

  return hori

def imagem_vertical():
  for i in range (10):
    if i == 0:
      vert = imagem_horizontal()
      continue
    else:
      vert2 = imagem_horizontal()
    vert = np.concatenate((vert, vert2), axis=0)

  return vert

for j in range(5):
  for z in range(5):
    if z == 0:
      imgFull = imagem_vertical()
      continue
    else:
      imgFull2 = imagem_vertical()
    imgFull = np.concatenate((imgFull, imgFull2), axis=1)
  titulo = ('./img_teste/teste'+(str(j+1))+'.png')
  cv2.imwrite(titulo,imgFull)

#cv2.imshow('COMPLETA', imgFull)
