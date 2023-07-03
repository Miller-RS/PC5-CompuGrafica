import cv2

# Inicializar la cámara
cam = cv2.VideoCapture(0)

# Cargar el clasificador de cascada preentrenado para la detección de Pokémon
clasificador = cv2.CascadeClassifier('cascade_pokemon.xml')

while True:
    # Leer el siguiente fotograma del video
    check, img = cam.read()

    # Convertir la imagen a escala de grises
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Detectar objetos (en este caso, Pokémon) en la imagen
    objetos = clasificador.detectMultiScale(imgGray, minSize=(60, 68), scaleFactor=5.5, minNeighbors=91)

    for x, y, l, a in objetos:
        # Dibujar un rectángulo alrededor del objeto detectado
        cv2.rectangle(img, (x, y), (x+l, y+a), (255, 0, 0), 2)

        # Agregar texto "pokemon" encima del rectángulo
        cv2.putText(img, 'pokemon', (x, y-10), 2, 0.7, (255, 0, 0), 2, cv2.LINE_AA)

    # Mostrar la imagen resultante en una ventana llamada "Imagen"
    cv2.imshow('Imagen', img)

    # Esperar 1 milisegundo y verificar si se presiona la tecla 'q' para salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas abiertas
cam.release()
cv2.destroyAllWindows()
