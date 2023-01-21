import sys

from PIL import Image

for i in range (0,400):
  desImg = (str(i+1)+'.jpg')
  localImg = ("D:/Documentos/Alcir Jr/Mestrado/Projeto/Proj-Mestrado/faces/"+desImg)
  imagem = Image.open(localImg)
  #imagem = Image.open("D:/Documentos/Alcir Jr/Mestrado/Projeto/Proj-Mestrado/faces/1.jpg")

  imagem = imagem.resize((24, 24), Image.ANTIALIAS)

  localImgNova = ('./faces24x24/'+(str(i+1))+'.png')
  imagem.save(localImgNova)
  #imagem.save('imagem-{}x{}.png'.format(imagem.size[0], imagem.size[1]))

  titImg = ((str(i+1))+'.png '+'1 0 0 23 23')
  titulo2 = ('faces24x24/'+titImg)
  with open("./faces24x24/pos.txt","a+") as info:
    info.write(titulo2+"\n")
    info.read()

  titImg = ((str(i+1))+'.png')
  titulo2 = ('faces24x24/'+titImg)
  with open("./faces24x24/neg.txt","a+") as bg:
    bg.write(titulo2+"\n")
    bg.read()