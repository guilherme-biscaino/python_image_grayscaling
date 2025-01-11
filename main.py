# %matplotlib inline
import datetime
import matplotlib.pyplot as plt # imports

# instanciação das imagens que serão tratadas
base_image = plt.imread('teste.jpg')
gray_image = base_image.copy()
binary_image = base_image.copy()

# inicio do contador de execução
print(datetime.datetime.now())

# i == Linha
# pixel == Pixel da linha
# [0][1][2] = Valores BGR do pixel


# LEIA-SE: Enquanto i (iterador) for menor que a altura da imagem faça:
i = 0
while i < len(base_image):
    # LEIA-SE: Para cada pixel na linha(fazendo referencia a linha que o iterador está)
    for pixel, value in enumerate(base_image[i]):

        # Soma dos valores RGB aplicando os pesos (segundo o metodo de grayscaling luminosity)
        gray = sum((value[0] * 0.07, value[1] * 0.72, value[2] * 0.21))

        # Define variável para binarização e seu valor mediante a condicional
        binary = 0 if gray < 130 else 255

        # A atribuição dos valores RGB no pixel
        gray_image[i][pixel][0], gray_image[i][pixel][1], gray_image[i][pixel][2] = gray, gray, gray 

        # A atribuição dos valores RGB no pixel
        binary_image[i][pixel][0], binary_image[i][pixel][1], binary_image[i][pixel][2] = binary, binary, binary

    # Aumenta o iterador, sinallizando a ida para a proxima linha
    i += 1

# arquivamento das imagens
plt.imsave('real_ou_fake2.jpg', gray_image)
plt.imsave('real_ou_fake3.jpg', binary_image)

# fim do contador de execução
print(datetime.datetime.now())
