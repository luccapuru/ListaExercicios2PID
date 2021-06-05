import cv2 
import numpy as np 

def Log(img):
    a = 255/np.log((1+np.ndarray.max(img)))
    imgLog = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(imgLog.shape[0]):
        for j in range(imgLog.shape[1]):
            g = round(a*np.log(img[i,j] + 1))
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            imgLog[i,j] = g
    return imgLog

def Exp(img):
    a = 255/np.log(1+np.ndarray.max(img)) #log inversa
    # a = 255/(np.e**np.ndarray.max(img) - 1)
    imgExp = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(imgExp.shape[0]):
        for j in range(imgExp.shape[1]):
            g = round((np.e**img[i,j] - 1)**(1/a))
            #print(g)
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            imgExp[i,j] = g
    return imgExp

def Quad(img):
    a = 255/ np.ndarray.max(img)**2
    imgQuad = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(imgQuad.shape[0]):
        for j in range(imgQuad.shape[1]):
            g = a*img[i][j]**2
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            imgQuad[i,j] = g
    return imgQuad

def Raiz(img):
    a = 255/ np.ndarray.max(img)**(1/2)
    imgRaiz = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(imgRaiz.shape[0]):
        for j in range(imgRaiz.shape[1]):
            g = a*img[i][j]**(1/2)
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            imgRaiz[i,j] = g
    return imgRaiz

#abrindo imagem em escala de cinza
img = cv2.imread("images//all_souls_000013.jpg", cv2.IMREAD_GRAYSCALE)
#mostrando a imagem orginal 
cv2.imshow("Imagem Original", img)
imgLog = Log(img)
imgExp = Exp(img)
imgQuad = Quad(img)
imgRaiz = Raiz(img)

cv2.imshow("Imagem - Log", imgLog)
cv2.imshow("Imagem - Exp", imgExp)
cv2.imshow("Imagem - Quad", imgQuad)
cv2.imshow("Imagem - Raiz", imgRaiz)

cv2.imwrite("results//ex02Log.jpg", imgLog)
cv2.imwrite("results//ex02Exp.jpg", imgExp)
cv2.imwrite("results//ex02Quad.jpg", imgQuad)
cv2.imwrite("results//ex02Raiz.jpg", imgRaiz)

cv2.waitKey()
