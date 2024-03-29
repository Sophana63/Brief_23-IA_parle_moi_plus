import openai
import azure.cognitiveservices.speech as speechsdk
import pyttsx3

# Configure OpenAI API
openai.api_key = "votre_key"

# Configure Azure Speech Services
speech_config = speechsdk.SpeechConfig(
    subscription="votre_key",
    region="votre_region"
)
speech_config.speech_synthesis_voice_name = "vi-VN-HoaiMyNeural"

# Create a speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="fr-CA")

# Start recognition and get a result
result = speech_recognizer.recognize_once()

# Use OpenAI API to process the recognized text in French
openai_response = openai.Completion.create(
    engine="ada",
    prompt=result.text,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.1
)

# Use pyttsx3 to read the response aloud


engine = pyttsx3.init()   
engine.say(openai_response.choices[0].text)
engine.runAndWait()

# Print the results
print("Texte reconnu :", result.text)
print("Réponse OpenAI :", openai_response.choices[0].text)
