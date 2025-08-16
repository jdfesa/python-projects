"""
translate_app.py
----------------
Pequeño traductor ES -> EN usando deep-translator (Google Translate).

Requisitos:
    - Paquete: deep-translator

Uso:
    Ejecuta el script y escribe la frase a traducir cuando se solicite.

Notas:
    - Si necesitas otros idiomas, ajusta `source` y `target`.
"""

from deep_translator import GoogleTranslator

def translate_text(text: str, source_lang: str = "es", target_lang: str = "en") -> str:
    """
    Traduce `text` desde `source_lang` a `target_lang` usando GoogleTranslator.
    Devuelve la cadena traducida o un mensaje de error legible.
    """
    text = (text or "").strip()
    if not text:
        return "⚠️ No ingresaste texto para traducir."

    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        return translator.translate(text)
    except Exception as exc:
        # Mensaje compacto y entendible para el usuario
        return f"❌ No se pudo traducir en este momento. Detalle: {exc.__class__.__name__}"

def main():
    print("Traductor ES → EN")
    user_input = input("¿Qué quieres traducir? ")
    result = translate_text(user_input, source_lang="es", target_lang="en")
    print(result)

if __name__ == "__main__":
    main()

