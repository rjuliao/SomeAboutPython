import numpy as np
import matplotlib.pyplot as plt
import cv2 as op

"""
Leemos la imagen en ecasa de grises
Cremos un vector de 256 posiciones que representa la intensidad del color
Lo siguiente es ir por cada pixel de la imagen y sumarlo en el vector cuya
posición corresponde con el valor del color.
Luego esos valores creamos el histograma.
"""

img = op.imread('child.jpg',op.IMREAD_GRAYSCALE)
width, height = img.shape
#Imagen en escala de grises que va desde 0-255
gray = np.zeros(256, dtype=np.int)

for i in range(width):
    for j in range(height):
        r = img[i,j]
        gray[r]+=1

y = np.arange(len(gray))

plt.bar( y, gray, color="red", alpha=0.5)
plt.title("")
plt.xlabel("Gama de colores en escala de grises")
plt.ylabel("Frencuencia")
plt.show()


op.imshow('Hola',img)
op.waitKey()
op.destroyAllWindows()
