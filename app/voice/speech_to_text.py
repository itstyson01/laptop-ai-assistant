import speech_recognition as sr




AUDIO_FILE = "recording.wav"


def speech_to_text():
    recognizer = sr.Recognizer()

    print("🧠 Converting speech to text...")

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = recognizer.record(source)
        

    try:
        text = recognizer.recognize_google(audio)

        print("📝 You said:", text)

        return text

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return ""

    except sr.RequestError as error:
        print("❌ Speech recognition service error:", error)
        return ""


if __name__ == "__main__":
    speech_to_text()