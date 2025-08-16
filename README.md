# python-projects
Colección de proyectos chicos en Python. **Cada proyecto incluye al inicio del archivo `.py` las instrucciones mínimas para instalar sus dependencias** (no hay `requirements.txt` global).

## Requisitos comunes
- Python 3.9+ (recomendado 3.10/3.11)
- Sugerido: entorno virtual  
  `python -m venv .venv && source .venv/bin/activate`  (en Windows: `.venv\Scripts\activate`)

---

## 1) Voice Recognition
Asistente por voz que pregunta la plataforma (**Mercado Libre** o **Amazon**), solicita el término y abre el navegador con la búsqueda.

- **Dependencias:** `SpeechRecognition`, `pyttsx3`, `pyaudio` *(requiere PortAudio)*.
- **Instalación rápida:** `pip install SpeechRecognition pyttsx3 pyaudio`  
  *(si PyAudio falla, instalar PortAudio en macOS/Linux o `pipwin install pyaudio` en Windows)*.
- **Uso:** `python app.py`
- **Opcional:** cambiar idioma en `listen(lang="es-AR")` y fijar micrófono con `dev=<índice>`.

---


## 2) Translate App
Traductor simple de español a inglés usando **GoogleTranslator** de `deep-translator`.

- **Dependencias:** `deep-translator`
- **Instalación rápida:** `pip install deep-translator`
- **Uso:** `python translate_app.py`  
  Escribir una frase en español y devuelve la traducción al inglés.

  ---
  

> Se irán agregando más mini-proyectos en este mismo repositorio.
