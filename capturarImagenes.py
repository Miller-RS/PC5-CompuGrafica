import cv2

# Inicializar la captura de video desde la cámara
video = cv2.VideoCapture(0)

# Inicializar un índice para nombrar las imágenes capturadas
index = 1

while True:
    # Leer el siguiente fotograma del video
    check, img = video.read()

    # Convertir la imagen a escala de grises
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if cv2.waitKey(1):
        print('bandera 1')

        # Redimensionar la imagen a un tamaño específico (36x48)
        imgR = cv2.resize(imgGray, (36, 48))

        # Guardar la imagen redimensionada en una carpeta llamada 'p' para imagenes positivas y 'n' para las imagenes negativas
        cv2.imwrite(f'p/{index}.jpg', imgR)

        # Incrementar el índice para el próximo nombre de imagen
        index += 1

    # Mostrar la imagen capturada en una ventana llamada "Captura"
    cv2.imshow('Captura', img)

    # Esperar 1 milisegundo y verificar si se presiona la tecla 'q' para salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar la captura de video y cerrar todas las ventanas abiertas
video.release()
cv2.destroyAllWindows()
