# Streamlit Speech-to-Text App using Vosk

This is a **real-time speech-to-text** web application built with **Streamlit** and **Vosk** for offline speech recognition.

## Features
- 🎤 **Click "Ask Question" to Start Listening**
- 🔊 **Recognizes Speech in Real-Time** using Vosk
- 📜 **Displays the Latest Recognized Speech**
- 📂 **Maintains a Conversation History**
- 🗑 **Clear Conversation with a Click**
- 🌐 **Runs in a Web Browser via Streamlit**

## Installation
### 1. Clone the Repository
```bash

git clone https://github.com/umang-algo/Speech-to-Text-App.git
cd Speech-to-Text-App
```

### 2. Install Dependencies
Make sure you have **Python 3.7+** installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Download and Set Up Vosk Model
Download a Vosk model from [Vosk Models](https://alphacephei.com/vosk/models) and extract it. Rename the folder to **`model`** and place it in the project directory.

For example:
```bash
mkdir model
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip -d model
```

### 4. Run the Application
```bash
streamlit run app.py
```

## Requirements
The project requires the following Python packages:
```txt
streamlit
pyaudio
vosk
```
If `pyaudio` installation fails, use:
```bash
pip install pipwin
pipwin install pyaudio
```

## Usage
- Click **"🎤 Ask Question"** to start listening.
- Speak clearly; your voice will be transcribed in real time.
- The **latest recognized speech** appears in a textbox.
- The **conversation history** is displayed below.
- Click **"Clear Conversation"** to reset the conversation.

## Troubleshooting
- If `pyaudio` fails to install, use `pipwin` as mentioned above.
- Ensure the **Vosk model folder** exists and is correctly named as `model`.
- If the microphone is not detected, check **audio input permissions**.

## License
This project is open-source under the **MIT License**.

## Author
Developed by **Your Name** – [GitHub Profile](https://github.com/your-username)

