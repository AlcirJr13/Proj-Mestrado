from locale import normalize

import cv2
import numpy as np

cascata = cv2.CascadeClassifier('cascade/cascade.xml')

atk_fn=0
atk_vp=0
nrm_fp=0
nrm_vn=0

for i in range (6500):
  Cam_foto = ('teste/ataque/ataque'+(str(i+1))+'.png')
  ataque = cv2.imread(Cam_foto)
  prev = cascata.detectMultiScale(
    ataque,
    scaleFactor=1.01,
    minNeighbors=5,
    minSize=(20,20),
    maxSize=(25,25),
    flags=0
  )
  if len(prev) == 0:
    atk_fn = atk_fn+1
  else:
    atk_vp = atk_vp+1
  del prev

for i in range (7150):
  Cam_foto = ('teste/normal/normal'+(str(i+1))+'.png')
  ataque = cv2.imread(Cam_foto)
  prev = cascata.detectMultiScale(
    ataque,
    scaleFactor=1.01,
    minNeighbors=10,
    minSize=(15,15),
    maxSize=(26,26),
    flags=0
  )
  if len(prev) == 0:
    nrm_vn = nrm_vn+1
  else:
    nrm_fp = nrm_fp+1
  del prev


msg1 = ('encontramos ' +(str(atk_vp)) + ' Verdadeiros positivos')
print(msg1)
msg1 = ('encontramos ' +(str(atk_fn)) + ' Falsos negativos')
print(msg1)
msg1 = ('encontramos ' +(str(nrm_vn)) + ' Verdadeiros negativos')
print(msg1)
msg1 = ('encontramos ' +(str(nrm_fp)) + ' Falsos positivos')
print(msg1)
