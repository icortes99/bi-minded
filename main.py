from utils.voice import listen_to_user, speak_to_user
from utils.nlp import get_ai_response
import config

def main():
  print("¡Bienvenido al asistente de idiomas!")
  while True:
    user_input = listen_to_user()
    print(f"Usuario dijo: {user_input}")

    if user_input.lower() in ["salir", "exit"]:
      speak_to_user("Goodbye! Adiós, amigo!", language=config.DEFAULT_TARGET_LANGUAGE)
      break

    response = get_ai_response(user_input, target_language=config.DEFAULT_TARGET_LANGUAGE)
    print(f"Asistente dice: {response}")

    speak_to_user(response, language=config.DEFAULT_TARGET_LANGUAGE)

if __name__ == "__main__":
  main()
