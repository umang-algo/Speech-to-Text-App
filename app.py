import streamlit as st
import pyaudio
import wave
import json
from vosk import Model, KaldiRecognizer

# Load Vosk Model (Ensure you have downloaded a Vosk model and set its path correctly)
MODEL_PATH = "model"
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Store recognized texts
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'is_listening' not in st.session_state:
    st.session_state.is_listening = False

def recognize_speech():
    """Function to recognize speech using Vosk."""
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    st.write("Listening... Speak clearly!")
    
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            stream.stop_stream()
            stream.close()
            p.terminate()
            return result.get("text", "Could not understand audio. Please try again.")

# Streamlit UI
st.title("Enhanced Speech-to-Text Conversation App")

# Ask a question button with mic icon
if st.button("🎤 Ask Question"):
    st.session_state.is_listening = True

if st.session_state.is_listening:
    recognized_text = recognize_speech()
    if recognized_text:
        st.session_state.conversation.append(recognized_text)
        st.session_state.is_listening = False  # Stop after recognizing

# Display text input box for latest response
st.write("### Recognized Text")
latest_text = st.session_state.conversation[-1] if st.session_state.conversation else ""
st.text_area("Latest Response:", value=latest_text, height=100)

# Display entire conversation history
st.write("### Conversation History")
full_conversation = "\n".join(st.session_state.conversation)
st.text_area("All Responses:", value=full_conversation, height=200)

# Clear conversation button
if st.button("Clear Conversation"):
    st.session_state.conversation = []