# Laptop AI Assistant 🤖

A Python-based voice assistant that can listen to your voice, convert speech into text, use Google Gemini to generate an AI response, and convert the response into speech.

## 🚀 Current Features

* 🎤 Voice recording using `sounddevice`
* 📝 Speech-to-text using `SpeechRecognition`
* 🤖 AI responses using Google Gemini
* 🔊 Text-to-speech from Gemini's response
* 🔐 API key management using `.env`
* 📦 Project dependencies managed with `requirements.txt`

## 🛠️ Tech Stack

* Python 3.13
* Google Gemini API
* `google-genai`
* `SpeechRecognition`
* `sounddevice`
* NumPy
* `python-dotenv`
* Text-to-Speech

## 📁 Project Structure

```text
laptop-ai-assistant/
│
├── app/
│   ├── ai/
│   │   └── gemini.py
│   │
│   └── voice/
│       ├── recorder.py
│       └── speech_to_text.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd laptop-ai-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the voice recorder

```bash
python app/voice/recorder.py
```

### 6. Convert the recording to text

```bash
python app/voice/speech_to_text.py
```

### 7. Test Gemini

```bash
python app/ai/gemini.py
```

## 🔒 Environment Variables

The Gemini API key is stored in `.env` and should **never be committed to GitHub**.

Make sure `.env` is included in `.gitignore`.

## 📌 Current Status

The assistant currently supports:

```text
🎤 Record voice
      ↓
📝 Speech-to-text
      ↓
🤖 Gemini AI response
      ↓
🔊 Text-to-speech
```

The complete voice-to-AI-to-voice pipeline is working.
