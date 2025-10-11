from googletrans import Translator

translator = Translator()

text = input("Enter text to translate: ")
target_lang = input("Enter target language code (e.g., 'en' for English, 'fr' for French): ")

translated = translator.translate(text, dest=target_lang)
print(f"Translated text ({target_lang}): {translated.text}")
