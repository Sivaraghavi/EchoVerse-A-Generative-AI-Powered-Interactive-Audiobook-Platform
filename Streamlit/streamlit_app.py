import streamlit as st
import speech_recognition as sr
import pyttsx3
from transformers import pipeline
import threading
import pdfplumber
import time

# Initialize text-to-speech engine with thread-safe handling
engine = pyttsx3.init()
engine_lock = threading.Lock()

# Initialize generative AI model (distilgpt2 for stability)
generator = pipeline('text-generation', model='distilgpt2', framework='pt')

# Predefined books with chapters
books = {
    "Harry Potter and the Sorcerer’s Stone": {
        0: "Chapter 1: Harry lived under the stairs at Privet Drive.",
        1: "Chapter 2: A letter arrived from Hogwarts, changing everything."
    },
    "Percy Jackson & The Lightning Thief": {
        0: "Chapter 1: Percy faced a monster on a school trip.",
        1: "Chapter 2: He discovered he was a demigod at Camp Half-Blood."
    },
    "The Mystery of the Lost Key": {
        0: "Chapter 1: The old house creaked as Jane found a dusty key.",
        1: "Chapter 2: A hidden door opened, revealing a dark secret."
    }
}

# Voice functions
def speak(text):
    def run_speech():
        with engine_lock:
            engine.say(text)
            engine.runAndWait()
    thread = threading.Thread(target=run_speech)
    thread.start()
    thread.join(timeout=10)  # Ensure thread completes within 10s

def get_voice_input():
    recognizer = sr.Recognizer()
    attempts = 0
    max_attempts = 2
    while attempts < max_attempts:
        with sr.Microphone() as source:
            st.write("🎙️ Listening... Speak now!")
            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                text = recognizer.recognize_google(audio)
                st.write(f"🗣️ You said: {text}")
                return text
            except sr.WaitTimeoutError:
                st.write("⏳ No speech detected. Trying again...")
                attempts += 1
            except sr.UnknownValueError:
                st.write("❌ Couldn’t understand. Try again!")
                return ""
            except sr.RequestError:
                st.write("🌐 Speech service down.")
                return ""
    st.write("❌ Max attempts reached. Type instead?")
    return st.text_input("Type your response:")

# Generative AI functions
def generate_response(user_input, chapter_text, past_interactions):
    context = f"Chapter: {chapter_text}\n"
    if past_interactions:
        context += "Past chat: " + "; ".join([i['response'] for i in past_interactions]) + "\n"
    prompt = f"{context}Friend says: '{user_input}'. Respond like a fun friend, using story details to debate or build a plot:"
    response = generator(prompt, max_length=80, num_return_sequences=1, temperature=0.95, truncation=True)[0]['generated_text']
    return response.replace(prompt, "").strip()[:150]

def generate_fanfiction(prompt, chapter_text, is_public):
    full_prompt = f"Based on '{chapter_text}', write a full chapter where {prompt}"
    chapter = generator(full_prompt, max_length=300, num_return_sequences=1, temperature=0.9, truncation=True)[0]['generated_text']
    return {"text": chapter.replace(full_prompt, "").strip(), "public": is_public, "timestamp": time.ctime()}

def generate_challenge(chapter_text):
    prompt = f"Based on '{chapter_text}', create a fun, tricky question and its answer:"
    qa = generator(prompt, max_length=100, num_return_sequences=1, truncation=True)[0]['generated_text']
    qa = qa.replace(prompt, "").strip().split("Answer:")
    return {"question": qa[0].strip(), "answer": qa[1].strip() if len(qa) > 1 else "Check the chapter!"}

def narrate_chapter(chapter_text):
    prompt = f"Narrate '{chapter_text}' in a dramatic, storytelling voice:"
    narration = generator(prompt, max_length=150, num_return_sequences=1, truncation=True)[0]['generated_text']
    return narration.replace(prompt, "").strip()

# Streamlit app
st.set_page_config(page_title="EchoVerse", page_icon="📖", layout="wide")
st.title("📚 EchoVerse: Your Interactive Audiobook Adventure")
st.markdown("Explore stories, chat with an AI buddy, and unleash your creativity!")

# Session state
if 'interactions' not in st.session_state:
    st.session_state.interactions = []
if 'fanfictions' not in st.session_state:
    st.session_state.fanfictions = []
if 'selected_book' not in st.session_state:
    st.session_state.selected_book = None
if 'custom_chapters' not in st.session_state:
    st.session_state.custom_chapters = {}

# Sidebar
with st.sidebar:
    st.header("📖 Your Story")
    book_option = st.radio("Mode:", ("Browse Books", "Upload PDF"), help="Pick a story or upload your own!")
    if book_option == "Browse Books":
        selected_book = st.selectbox("Choose a Book", list(books.keys()))
        st.session_state.selected_book = selected_book
        chapters = books[selected_book]
    else:
        uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
        if uploaded_file:
            with pdfplumber.open(uploaded_file) as pdf:
                text = "".join(page.extract_text() or "" for page in pdf.pages)
                paragraphs = text.split("\n\n")
                st.session_state.custom_chapters = {i: f"Chapter {i+1}: {p[:100]}..." for i, p in enumerate(paragraphs[:2])}
            chapters = st.session_state.custom_chapters
            st.session_state.selected_book = uploaded_file.name
        else:
            st.info("Upload a PDF to begin!")
            chapters = {}

# Main content
if chapters:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"📖 {st.session_state.selected_book}")
        chapter_index = st.selectbox("Pick a Chapter", list(chapters.keys()), format_func=lambda x: f"Chapter {x+1}")
        chapter_text = chapters[chapter_index]
        st.markdown(f"**{chapter_text}**")
        
        if st.button("🎙️ Hear Narration", help="Listen to an AI-narrated version!"):
            narration = narrate_chapter(chapter_text)
            st.write(f"🎭 Narration: {narration}")
            speak(narration)

        # Chat with AI Friend
        st.subheader("🗣️ Chat with Your AI Buddy")
        if st.button("🎤 Speak Now", help="Chat about the chapter!"):
            user_response = get_voice_input()
            if user_response:
                ai_response = generate_response(user_response, chapter_text, st.session_state.interactions)
                st.success(f"🤖 Buddy: {ai_response}")
                speak(ai_response)
                st.session_state.interactions.append({"chapter": chapter_text, "response": user_response})

        # Fanfiction
        st.subheader("✍️ Write a Chapter")
        fanfiction_prompt = st.text_input("Start your chapter (e.g., 'Harry finds a secret...')")
        visibility = st.radio("Visibility:", ("Public", "Private"), horizontal=True)
        if st.button("✨ Generate Chapter", help="Create a full chapter!"):
            if fanfiction_prompt:
                fanfiction = generate_fanfiction(fanfiction_prompt, chapter_text, visibility == "Public")
                st.info(f"📜 Your Chapter ({'Public' if fanfiction['public'] else 'Private'}):\n{fanfiction['text']}")
                speak(fanfiction['text'][:100])  # Speak first 100 chars
                st.session_state.fanfictions.append(fanfiction)

    with col2:
        # Dynamic Challenge
        st.subheader("🎯 Story Challenge")
        if st.button("🔄 New Challenge", help="Get a fresh question!"):
            challenge = generate_challenge(chapter_text)
            st.session_state.challenge = challenge
        if 'challenge' in st.session_state:
            user_answer = st.text_input(st.session_state.challenge['question'])
            if st.button("✅ Check Answer"):
                if user_answer.lower() in st.session_state.challenge['answer'].lower():
                    st.success("🎉 Nailed it!")
                    speak("Awesome job!")
                else:
                    st.warning("❌ Not quite! Try again.")
                    speak("Give it another shot!")

        # Fanfiction Library
        if st.session_state.fanfictions:
            st.subheader("🌐 Fanfiction Library")
            for i, story in enumerate(st.session_state.fanfictions):
                if story['public'] or story in [f for f in st.session_state.fanfictions if f['timestamp'] == story['timestamp']]:
                    st.write(f"Story {i+1} ({'Public' if story['public'] else 'Private'} - {story['timestamp']}):")
                    with st.expander("Read Chapter"):
                        st.write(story['text'])

        # Wrap-Up
        st.subheader("🏆 Your Adventure")
        if st.button("📊 View Wrap-Up"):
            st.write("**Your Chats:**")
            for i, interaction in enumerate(st.session_state.interactions):
                st.write(f"- Chapter {i+1}: {interaction['chapter'][:20]}... - You: {interaction['response']}")
            if st.session_state.fanfictions:
                st.write("**Your Chapters:**")
                for i, story in enumerate(st.session_state.fanfictions):
                    st.write(f"- Story {i+1} ({'Public' if story['public'] else 'Private'}): {story['text'][:50]}...")
            speak("Here’s your epic wrap-up!")

# Footer
st.markdown("---")
st.write("Made with ❤️ by [Your Name] for KUKU FM | Powered by AI")