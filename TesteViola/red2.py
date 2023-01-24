import sys

from PIL import Image

for i in range (0,100):
  desImg = (str(i+1)+'.jpg')
  localImg = ("D:/Documentos/Alcir Jr/Mestrado/Projeto/Proj-Mestrado/TesteViola/negativo/"+desImg)
  imagem = Image.open(localImg)


  imagem = imagem.resize((260, 360), Image.ANTIALIAS)

  localImgNova = ('./negativo_mod/'+(str(i+1))+'.jpg')
  imagem.save(localImgNova)


  titImg = ((str(i+1))+'.jpg')
  titulo2 = ('negativo_mod/'+titImg)
  with open("./negativo_mod/neg.txt","a+") as bg:
    bg.write(titulo2+"\n")
    bg.read()