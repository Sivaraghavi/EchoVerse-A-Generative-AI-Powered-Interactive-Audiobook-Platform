
# from transformers import pipeline
# import speech_recognition as sr
# import pyttsx3

# try:
#     generator = pipeline('text-generation', model='distilgpt2', framework='pt')
# except Exception as e:
#     print(f"Error loading AI model: {e}")
#     generator = None

# engine = pyttsx3.init()

# def generate_response(user_input, chapter_text, past_interactions):
#     if not generator:
#         return "AI model not available. Please try again later."
#     context = f"Chapter: {chapter_text}\nPast chat: {'; '.join(past_interactions)}\nYou: {user_input}\nAI Buddy:"
#     try:
#         response = generator(context, max_length=100, num_return_sequences=1, temperature=0.95, truncation=True)[0]['generated_text']
#         return response.split("AI Buddy:")[-1].strip()
#     except Exception as e:
#         return f"Error generating response: {str(e)}"

# def generate_fanfiction(book, chapters, user_prompt):
#     if not generator:
#         return ["AI model not available.", "Please try again later.", "Contact support."]
#     full_story = " ".join(chapters.values())
#     prompt = f"Based on '{book}', where {user_prompt}, write a 3-chapter fanfiction:"
#     try:
#         fanfic = generator(prompt, max_length=500, num_return_sequences=1, temperature=0.9, truncation=True)[0]['generated_text']
#         chapters = fanfic.split("Chapter ")[1:] if "Chapter " in fanfic else [fanfic] * 3
#         return chapters[:3]  # Ensure exactly 3 chapters
#     except Exception as e:
#         return [f"Error: {str(e)}"] * 3

# def get_voice_input():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening... Please speak now.")
#         try:
#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
#             return recognizer.recognize_google(audio)
#         except sr.WaitTimeoutError:
#             return "Timeout: No speech detected."
#         except sr.UnknownValueError:
#             return "Error: Couldn’t understand speech."
#         except Exception as e:
#             return f"Error: {str(e)}"

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Text-to-speech error: {e}")

# # from transformers import pipeline
# # import speech_recognition as sr
# # import pyttsx3
# # import torch

# # # Initialize AI models and voice engine
# # try:
# #     device = "cuda" if torch.cuda.is_available() else "cpu"
# #     generator = pipeline('text-generation', 
# #                         model='distilgpt2', 
# #                         framework='pt',
# #                         device=device)
# # except Exception as e:
# #     print(f"Error loading AI model: {e}")
# #     generator = None

# # # Initialize text-to-speech engine
# # try:
# #     engine = pyttsx3.init()
# #     engine.setProperty('rate', 150)
# #     engine.setProperty('volume', 0.9)
# # except Exception as e:
# #     print(f"Error initializing TTS engine: {e}")
# #     engine = None

# # def generate_response(user_input, chapter_text, past_interactions):
# #     """Generate AI response using the context of the book chapter"""
# #     if not generator:
# #         return "AI model not available. Please try again later."
    
# #     # Create context for the AI
# #     context = (
# #         f"Chapter Context: {chapter_text}\n"
# #         f"Previous Interactions: {'; '.join(past_interactions)}\n"
# #         f"User: {user_input}\n"
# #         f"AI Buddy:"
# #     )
    
# #     try:
# #         response = generator(
# #             context,
# #             max_length=150,
# #             num_return_sequences=1,
# #             temperature=0.85,
# #             top_p=0.9,
# #             repetition_penalty=1.1,
# #             truncation=True
# #         )[0]['generated_text']
        
# #         # Extract only the AI's response
# #         return response.split("AI Buddy:")[-1].strip()
# #     except Exception as e:
# #         return f"Error generating response: {str(e)}"

# # def generate_fanfiction(book, chapters, user_prompt):
# #     """Generate fanfiction based on book content and user prompt"""
# #     if not generator:
# #         return ["AI model not available.", "Please try again later.", "Contact support."]
    
# #     full_story = " ".join(chapters.values())
# #     prompt = (
# #         f"Based on the book '{book}', where {user_prompt}, "
# #         f"write a creative 3-chapter fanfiction. Here's the original story context:\n"
# #         f"{full_story}\n\n"
# #         f"Fanfiction Story:"
# #     )
    
# #     try:
# #         fanfic = generator(
# #             prompt,
# #             max_length=800,
# #             num_return_sequences=1,
# #             temperature=0.7,
# #             top_p=0.85,
# #             repetition_penalty=1.05,
# #             truncation=True
# #         )[0]['generated_text']
        
# #         # Split into chapters
# #         if "Chapter 1" in fanfic and "Chapter 2" in fanfic:
# #             chapters = fanfic.split("Chapter ")[1:]
# #             chapters = [f"Chapter {ch.strip()}" for ch in chapters]
# #         else:
# #             chapters = [fanfic] * 3
            
# #         return chapters[:3]  # Ensure exactly 3 chapters
# #     except Exception as e:
# #         return [f"Error: {str(e)}"] * 3

# # def get_voice_input():
# #     """Capture voice input from microphone"""
# #     if not engine:
# #         return "Text-to-speech not available"
    
# #     recognizer = sr.Recognizer()
# #     recognizer.energy_threshold = 300
# #     recognizer.pause_threshold = 0.8
    
# #     with sr.Microphone() as source:
# #         print("Calibrating microphone...")
# #         recognizer.adjust_for_ambient_noise(source, duration=1)
# #         print("Listening... Please speak now.")
        
# #         try:
# #             audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
# #             text = recognizer.recognize_google(audio)
# #             print(f"Recognized: {text}")
# #             return text
# #         except sr.WaitTimeoutError:
# #             return "Timeout: No speech detected."
# #         except sr.UnknownValueError:
# #             return "Error: Couldn't understand speech."
# #         except sr.RequestError as e:
# #             return f"Error: Speech service unavailable - {str(e)}"
# #         except Exception as e:
# #             return f"Error: {str(e)}"

# # def speak(text):
# #     """Convert text to speech"""
# #     if not engine:
# #         print("Text-to-speech engine not available")
# #         return
    
# #     try:
# #         engine.say(text)
# #         engine.runAndWait()
# #     except Exception as e:
# #         print(f"Text-to-speech error: {e}")

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