import cv2 
import numpy as np 


def Limiar(img, limiar):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] >= limiar:
                img[i][j] = 255
            else:
                img[i][j] = 0
    
#abrindo imagem em escala de cinza
# img = cv2.imread("images//all_souls_000013.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("images//mari.jpg", cv2.IMREAD_GRAYSCALE)
#mostrando a imagem orginal 
cv2.imshow("Imagem Original", img)
limiar = input("Digite o valor do Limiar: ")
Limiar(img, int(limiar))
cv2.imshow("Imagem Limiarizada", img)
# cv2.imwrite("results//ex01high.jpg", img)
cv2.waitKey()
