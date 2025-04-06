from transformers import pipeline
import speech_recognition as sr
import pyttsx3

generator = pipeline('text-generation', model='distilgpt2')
engine = pyttsx3.init()

def generate_response(user_input, chapter_text, past_interactions):
    context = f"Chapter: {chapter_text}\nPast chat: {'; '.join(past_interactions)}\nYou: {user_input}\nAI Buddy:"
    response = generator(context, max_length=100, num_return_sequences=1, temperature=0.95, truncation=True)[0]['generated_text']
    return response.split("AI Buddy:")[-1].strip()

def generate_fanfiction(book, chapters, user_prompt):
    full_story = " ".join(chapters.values())
    prompt = f"Based on '{book}', where {user_prompt}, write a 3-chapter fanfiction:"
    fanfic = generator(prompt, max_length=500, num_return_sequences=1, temperature=0.9, truncation=True)[0]['generated_text']
    if "Chapter " in fanfic:
        return fanfic.split("Chapter ")[1:]
    else:
        return [fanfic, fanfic, fanfic]

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            return "Timeout: No speech detected."
        except sr.UnknownValueError:
            return "Error: Couldn’t understand speech."
        except Exception as e:
            return f"Error: {str(e)}"

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text-to-speech error: {e}")
