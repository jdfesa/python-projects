# deps: pip install SpeechRecognition pyttsx3 pyaudio

import speech_recognition as sr
import pyttsx3
import webbrowser, sys, subprocess
from urllib.parse import quote_plus

r = sr.Recognizer()
t = pyttsx3.init()

def speak(s):
    t.say(s); t.runAndWait()

def listen(lang="es-AR", dev=None):
    # Si no sabés el índice del micrófono, mirá el print que sale una vez
    if dev is None:
        try:
            names = sr.Microphone.list_microphone_names()
            print("Micrófonos disponibles:", {i: n for i, n in enumerate(names)})
        except Exception:
            pass

    mic_kwargs = {} if dev is None else {"device_index": dev}

    r.dynamic_energy_threshold = True
    r.energy_threshold = 200
    r.pause_threshold = 0.7
    r.non_speaking_duration = 0.4

    with sr.Microphone(**mic_kwargs) as src:
        print("🎙️ Escuchando...")
        r.adjust_for_ambient_noise(src, duration=0.6)
        try:
            audio = r.listen(src, timeout=6, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("No se detectó voz a tiempo.")
            return None

    try:
        txt = r.recognize_google(audio, language=lang).strip().lower()
        print("Has dicho:", txt)
        return txt
    except sr.UnknownValueError:
        print("No entendí (audio poco claro).")
        return None
    except sr.RequestError as e:
        print("Error del servicio:", e)
        return None


if __name__ == "__main__":
    speak("Decime Mercado Libre o Amazon.")
    cmd = listen()

    if cmd and ("mercado libre" in cmd or "mercadolibre" in cmd):
        speak("¿Qué querés buscar?")
        q = listen()
        if q:
            from urllib.parse import quote_plus
            import sys, subprocess, webbrowser
            url = f"https://listado.mercadolibre.com.ar/{quote_plus(q)}"
            if sys.platform == "darwin":
                subprocess.run(["open", url])   # macOS
            else:
                webbrowser.open(url, new=2)
            speak(f"Buscando {q} en Mercado Libre.")
    elif cmd and "amazon" in cmd:
        speak("¿Qué querés buscar?")
        q = listen()
        if q:
            from urllib.parse import quote_plus
            import sys, subprocess, webbrowser
            url = f"https://www.amazon.es/s?k={quote_plus(q)}"
            if sys.platform == "darwin":
                subprocess.run(["open", url])
            else:
                webbrowser.open(url, new=2)
            speak(f"Buscando {q} en Amazon.")
    else:
        speak("No entendí.")
