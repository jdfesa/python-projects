# os.path.join(os.path.dirname(__file__), "alarma_python.mp3")


# pip install playsound==1.2.2
import os
import time
from playsound import playsound

# 🔔 Cantidad de veces que debe sonar la alarma
REPETICIONES = 3   # podés cambiar este valor

def alarma(minutes, seconds):
    sound_path = os.path.join(os.path.dirname(__file__), "alarma_python.mp3")

    total_seconds = minutes * 60 + seconds
    print(f"La alarma sonará en {minutes} minutos y {seconds} segundos.")

    time.sleep(total_seconds)

    # reproducir en bucle REPETICIONES veces
    for i in range(REPETICIONES):
        print(f"⏰ Alarma {i+1}/{REPETICIONES}")
        playsound(sound_path)

# --- entrada de usuario ---
minutes = int(input("Ingresa los minutos de la alarma: "))
seconds = int(input("Ingresa los segundos de la alarma: "))

alarma(minutes, seconds)
