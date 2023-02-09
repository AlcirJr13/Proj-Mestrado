from locale import normalize

import cv2
import numpy as np

cascata = cv2.CascadeClassifier('cascade/cascade.xml')
#ataque = cv2.imread("ataques6x6/ataque19.png")
#normal = cv2.imread("normal/normal1.png")

#teste = cascata.detectMultiScale(ataque)
#teste2 = cascata.detectMultiScale(normal)

#print(teste)
j=0

for i in range (400):
  Cam_foto = ('faces/'+(str(i+1))+'.jpg')
  #print(Cam_foto)
  ataque = cv2.imread(Cam_foto)
  #prev = cascata.detectMultiScale(ataque)
  prev = cascata.detectMultiScale(
    ataque,
    scaleFactor=1.01,
    minNeighbors=3,
    minSize=(100,200),
    maxSize=(270,370),
    flags=0
  )
  if len(prev) == 0:
    print("sem ataque")
  else:
    j = j+1
  del prev

msg = ('encontramos ' +(str(j)) + ' ataques')
print(msg)