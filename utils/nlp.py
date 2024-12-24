from openai import OpenAI
from langdetect import detect
import config

client = OpenAI(api_key = config.OPENAI_API_KEY)

def get_ai_response(prompt, target_language = config.DEFAULT_TARGET_LANGUAGE):
  try:
    response = client.chat.completions.create(
      model = "gpt-4o-mini",
      messages=[
        {
          "role": "user",
          "content": "This is an app to learn a new language. This user is a Spanish native speaker and is trying to learn English. Progressively go switching to english in your answers. This is what the user is saying: " + prompt
        }
      ],
    )
    ai_response = response.choices[0].message.content

    #if detect(prompt) != target_language:
      #ai_response = translate_text(ai_response, target_language)

    return ai_response
  except Exception as e:
    return f"Error procesando la solicitud: {e}"

def translate_text(text, target_language):
  return f"(Traducción a {target_language} no implementada aún): {text}"
