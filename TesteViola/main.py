import cv2

imagem = cv2.imread("ataques/a1.png")
#imagem = cv2.imread("./imagens/ataques/ataque4.png")
cv2.imshow("Original", imagem)
cv2.waitKey(0)
