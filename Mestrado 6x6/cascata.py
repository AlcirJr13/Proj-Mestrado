from locale import normalize

import cv2
import numpy as np

cascata = cv2.CascadeClassifier('cascade/cascade.xml')

j=0

for i in range (10):
  Cam_foto = ('img_teste/teste'+(str(i+1))+'.png')
  #print(Cam_foto)
  ataque = cv2.imread(Cam_foto)
  prev = cascata.detectMultiScale(
    ataque,
    scaleFactor=1.01,
    minNeighbors=3,
    minSize=(6,6),
    maxSize=(6,6),
    flags=0
  )
  if len(prev) == 0:
    print("sem ataque")
  else:
    print('ataque')
    for (x, y, w, h) in prev:
      cv2.rectangle(ataque, (x, y), (x+w, y+h), (255, 0, 0), 1)
    #cv2.imshow('',ataque)
    #cv2.waitKey(0)
    titulo = ('./img_teste/detec'+(str(i+1))+'.png')
    cv2.imwrite(titulo,ataque)
  #del prev

print('fim')