# EchoVerse: Generative AI-Powered Interactive Audiobook and Fan Fiction Storyline Generator Prototype

Welcome to **EchoVerse**, an innovative project developed by Sivaraghavi as a prototype for Kuku FM. EchoVerse leverages generative AI to create personalized and collaborative audiobook experiences, including interactive storytelling, fan fiction generation, and community-driven narratives. This repository contains two implementations: a Dash-based web application and a Streamlit-based collaborative tool, designed to enhance user engagement on the Kuku FM platform.

## Project Overview
EchoVerse aims to revolutionize the audiobook experience by integrating AI-driven features such as:
- **Personalized Story Weaver**: Generates unique audio narratives based on user preferences, mood, and creative inputs.
- **Collaborative Story Jam**: Enables real-time, community-driven storytelling with AI moderation.
- **Interactive AI Buddy**: Facilitates reflective conversations about books.
- **Fan Fiction Generation**: Creates custom 3-chapter stories from user prompts.
- **Dashboard and Streaks**: Tracks user activity and motivates consistent usage.

The project targets a 20% increase in average daily time spent and a 15% increase in app open frequency on Kuku FM within six months.

## Repository Structure
- `app.py`: Main Dash application with story selection, narration, AI chat, fan fiction, and dashboard features.
- `Streamlit/streamlit_app.py`: Streamlit application for the Collaborative Story Jam feature.
- `venv/`: Virtual environment directory (optional, created locally).
- `echoverse.db`: SQLite database file (generated on first run).
- `README.md`: This file.

## Features
### Dash-Based Prototype (echoverse.py)
- **Story Selection and Narration**: Select predefined books (e.g., "Harry Potter and the Sorcerer’s Stone") or upload PDFs, with text-to-speech narration.
- **AI Buddy Chat**: Engage in text or voice-based conversations with contextual AI responses using DistilGPT-2.
- **Fan Fiction Generation**: Generate 3-chapter fan fiction from user prompts, with public/private options.
- **Collaborative Story Jam**: Contribute to a shared story via text or voice, enhanced by AI suggestions.
- **Dashboard**: Tracks streaks, visualizes interaction history with a Plotly graph, and recommends books.
- **Authentication**: Includes a simple login input (placeholder for real user authentication).

### Streamlit-Based Prototype (streamlit_app.py)
- **Real-Time Collaboration**: Users add to a shared story via text or voice input.
- **AI Moderation**: DistilGPT-2 generates narrative suggestions.
- **Voice Interaction**: Supports voice input and text-to-speech (with gTTS fallback if pyttsx3 fails).
- **Participant Tracking**: Displays the number of contributors.

## Setup Instructions
### Prerequisites
- Python 3.7+ (recommended: Python 3.9 or 3.10 for compatibility).
- Internet connection (for gTTS and transformers model downloads).

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/EchoVerse.git
   cd EchoVerse
   ```
2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   ```
3. **Install Dependencies:**
   ```bash
   pip install dash transformers speechrecognition pyttsx3 pdfplumber sqlite3 plotly streamlit gTTS
   ```
   This ensures compatibility for both Dash and Streamlit apps. If any package fails to install (e.g., due to Python version issues), try:
   
   ```bash
   pip install --upgrade pip
   pip install wheel
   pip install dash transformers speechrecognition pyttsx3 pdfplumber sqlite3 plotly streamlit gTTS
   ```
