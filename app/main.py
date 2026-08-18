import asyncio

from ai.gemini import ask_gemini
from voice.speech_to_text import speech_to_text
from voice.text_to_speech import text_to_speech
from voice.recorder import record_audio

audio = record_audio()

print("Audio shape:", audio.shape)

speech_text = speech_to_text()

response = ask_gemini(prompt=speech_text)

print(response)

asyncio.run(text_to_speech(response))