# importar as bibliotecas necessárias
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np

# importar o conjunto de dados MNIST
dataset = fetch_openml("MNIST Original")
(data, labels) = (dataset.data, dataset.target)

# Exibir algumas informações do dataset MNIST
print("[INFO] Número de imagens: {}".format(data.shape[0]))
print("[INFO] Pixels por imagem: {}".format(data.shape[1]))

# escolher um índice aleatório do dataset e exibir
# a imagem e label correspondente
np.random.seed(17)
randomIndex = np.random.randint(0, data.shape[0])
print("[INFO] Imagem aleatória do MNIST com label '{:.0f}':".format(labels[randomIndex]))

plt.imshow(data[randomIndex].reshape((28,28)), cmap="Greys")
plt.show()