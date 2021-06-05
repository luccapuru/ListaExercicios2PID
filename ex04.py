import cv2 
import numpy as np 

def EqHist(img):
    #calculando histograma
    h = np.zeros(256, np.int32)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            h[img[i,j]] += 1
    size = img.shape[0]*img.shape[1]
    print("s", size)
    probAc = []
    probSoma = 0
    for i in h:
        probSoma += i/size
        probAc.append(probSoma)
    probAc = [p*255 for p in probAc]
    probAc = np.array(probAc).astype(np.uint8)
    print(probAc)
    img2 = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            img2[i,j] = probAc[img[i,j]]
    return img2

    
    

# img = cv2.imread("images//all_souls_000013.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("images//all_souls_000005.jpg", cv2.IMREAD_GRAYSCALE)
#mostrando a imagem orginal 
cv2.imshow("Imagem Original", img)
img2 = EqHist(img)
cv2.imshow("Imagem Transformada", img2)
cv2.imwrite("results//ex04.jpg", img2)
cv2.waitKey()

