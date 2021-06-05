import cv2 
import numpy as np 

def Transform(img):
    aLog = 255/np.log((1+np.ndarray.max(img)))
    aExp = 255/np.log(1+np.ndarray.max(img))
    img2 = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            if img[i][j] < 128: #Exp
                g = round((np.e**img[i,j] - 1)**(1/aExp))
            else: #Log
                g = round(aLog*np.log(img[i,j] + 1))
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            img2[i,j] = g
    return img2

img = cv2.imread("images//all_souls_000013.jpg", cv2.IMREAD_GRAYSCALE)
#mostrando a imagem orginal 
cv2.imshow("Imagem Original", img)
img2 = Transform(img)
cv2.imshow("Imagem Transformada", img2)
cv2.imwrite("results//ex03.jpg", img2)
cv2.waitKey()