# el problema por el cual no estaba lleyendo el archivo es porque estaba en la misma carpeta, lo saque y lo puse afuera y todo funciono de maravilla
from translate import Translator

with open("message.txt", "r") as my_message:
    message_text = my_message.read()
    print(f"Mensaje original: {message_text}")
    print("Translating...")
    translator = Translator(to_lang="es")
    translation = translator.translate(message_text)
    print(f"Mensaje traducido: {translation}")

    with open('translated_message.txt', 'w') as my_translation:
        text = my_translation.write(translation)