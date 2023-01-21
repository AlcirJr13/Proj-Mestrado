from tkinter import *

from PIL import Image, ImageTk

# Criando Objeto Tkinter
root = Tk()

image = Image.open("D:/Documentos/Alcir Jr/Mestrado/Projeto/Proj-Mestrado/faces/1.jpg")

# Resize the image using resize() method
resize_image = image.resize((580, 580))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

# Execute Tkinter
root.mainloop()