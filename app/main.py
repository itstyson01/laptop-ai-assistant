import asyncio

from ai.gemini import ask_gemini
from voice.speech_to_text import speech_to_text
from voice.text_to_speech import text_to_speech
from voice.recorder import record_audio
from voice.wake_word import wait_for_wake_word


while True:

    # Wait for wake word
    wait_for_wake_word()

    print("Assistant activated!")

    # Record user's command
    audio = record_audio()

    print("Audio shape:", audio.shape)

    # Convert speech to text
    speech_text = speech_to_text()

    print("You:", speech_text)

    # Send text to Gemini
    response = ask_gemini(prompt=speech_text)

    print("Gemini:", response)

    # Convert Gemini response to voice
    asyncio.run(text_to_speech(response))