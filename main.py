import os
import time
import cv2

# Ruta al archivo de video
ruta_video = "kira.mp4"

# Función para reproducir el video
def reproducir_video(ruta_video):
    # Cargar el video
    cap = cv2.VideoCapture(ruta_video)
    
    # Reproducir el video frame por frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        
        # Presionar 'q' para cerrar el video antes
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Reproduce el video
reproducir_video(ruta_video)

# Duración de tiempo para abrir el Bloc de notas en segundos
tiempo_total = 10
# Momento en el que comienza la ejecución
inicio = time.time()

# Ejecuta mientras no hayan pasado los 10 segundos
while time.time() - inicio < tiempo_total:
    os.system("start notepad")
    time.sleep(1)  # Espera 1 segundo antes de abrir otro Bloc de notas

print("Ejecución finalizada. Apagando el sistema...")

# Comando para apagar la PC en Windows
os.system("shutdown /s /t 1")
